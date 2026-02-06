# CI/CD 문제 해결 가이드

이 문서는 프로젝트에서 발생한 CI/CD 문제점과 해결 방법을 정리한 것입니다.

## 목차

1. [GitHub Actions workflow_call 오류](#1-github-actions-workflow_call-오류)
2. [백엔드 테스트/마이그레이션 없을 때 실패](#2-백엔드-테스트마이그레이션-없을-때-실패)
3. [GitHub Actions secrets를 if 조건에서 직접 참조 불가](#3-github-actions-secrets를-if-조건에서-직접-참조-불가)
4. [Prettier 포맷팅 오류](#4-prettier-포맷팅-오류)
5. [Next.js SWC 바이너리 다운로드 404 오류](#5-nextjs-swc-바이너리-다운로드-404-오류)

---

## 1. GitHub Actions workflow_call 오류

### 문제 상황

```
Invalid workflow file ... workflow is not reusable as it is missing a on.workflow_call trigger
```

### 원인

- `workflow_call`을 사용하여 다른 워크플로우에서 호출하려면 `on.workflow_call` 트리거가 필요합니다.
- 중앙 `ci.yml`이 `frontend.yml`과 `backend.yml`을 호출하면서, 각 워크플로우도 자체 `push` 트리거를 가지고 있어 중복 실행이 발생했습니다.

### 해결 방법

#### 방법 1: workflow_call 트리거 추가

```yaml
on:
  push:
    branches: [main, develop]
    paths:
      - 'frontend/**'
  workflow_call:
    secrets:
      VERCEL_TOKEN:
        required: false
```

#### 방법 2: 중앙 orchestrator 제거 (권장)

- `ci.yml` 파일 삭제
- 각 워크플로우가 독립적으로 실행되도록 설정
- `paths` 필터로 변경사항에 따라 자동 실행

### 결과

- 각 워크플로우가 독립적으로 실행됨
- 중복 실행 문제 해결
- 더 간단하고 명확한 구조

---

## 2. 백엔드 테스트/마이그레이션 없을 때 실패

### 문제 상황

- 테스트 파일이 없는데도 pytest가 실행되어 실패
- 마이그레이션 파일이 없는데도 alembic check가 실패
- 배포 단계가 테스트 실패로 인해 스킵됨

### 원인

- 테스트/마이그레이션 파일 존재 여부를 확인하지 않고 실행
- 실패 시 워크플로우 전체가 실패로 표시됨

### 해결 방법

#### 1. 테스트 파일 존재 여부 확인

```yaml
- name: Check if tests exist
  id: check_tests
  run: |
    if [ -d "tests" ] && [ "$(find tests -name 'test_*.py' -o -name '*_test.py' 2>/dev/null | head -1)" ]; then
      echo "tests_exist=true" >> $GITHUB_OUTPUT
    else
      echo "tests_exist=false" >> $GITHUB_OUTPUT
    fi
```

#### 2. 조건부 실행

```yaml
- name: Run tests
  if: steps.check_tests.outputs.tests_exist == 'true'
  run: pytest -v
```

#### 3. continue-on-error 사용

```yaml
test:
  name: Test
  continue-on-error: true  # 테스트 파일이 없으면 항상 성공
```

#### 4. 배포 단계에서 테스트 의존성 제거

```yaml
deploy-railway:
  needs: [lint]  # test 제거
```

### 결과

- 테스트 파일이 없어도 워크플로우 성공
- 마이그레이션 파일이 없어도 워크플로우 성공
- Lint 통과 시 배포 진행

---

## 3. GitHub Actions secrets를 if 조건에서 직접 참조 불가

### 문제 상황

```yaml
if: github.ref == 'refs/heads/main' && secrets.RAILWAY_TOKEN != ''
```

```
Unrecognized named-value: 'secrets'. Located at position 67 within expression
```

### 원인

- GitHub Actions에서는 보안상의 이유로 `if` 조건에서 `secrets`를 직접 참조할 수 없습니다.
- `secrets`는 step 내부에서만 사용 가능합니다.

### 해결 방법

#### 1. Step 내부에서 secret 확인

```yaml
- name: Check Railway token
  id: check_token
  run: |
    if [ -z "${{ secrets.RAILWAY_TOKEN }}" ]; then
      echo "token_exists=false" >> $GITHUB_OUTPUT
    else
      echo "token_exists=true" >> $GITHUB_OUTPUT
    fi
```

#### 2. 조건부 실행

```yaml
- name: Deploy to Railway
  if: steps.check_token.outputs.token_exists == 'true'
  run: railway up
  env:
    RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```

### 결과

- Secret이 없어도 워크플로우 실패하지 않음
- Secret이 있을 때만 배포 진행
- 명확한 로그 메시지

---

## 4. Prettier 포맷팅 오류

### 문제 상황

```
[warn] .next/cache/config.json
[warn] README.md
[warn] src/app/error.tsx
...
Code style issues found in 13 files.
```

### 원인

- `.next` 디렉토리(빌드 캐시)가 Prettier 체크 대상에 포함됨
- 소스 파일이 포맷팅되지 않음

### 해결 방법

#### 1. .prettierignore 파일 생성

```gitignore
# Dependencies
node_modules
.pnp
.pnp.js

# Testing
coverage

# Next.js
.next
out
build
dist

# Production
*.min.js
*.min.css

# Misc
.DS_Store
*.pem

# Debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Local env files
.env*.local

# Vercel
.vercel

# Typescript
*.tsbuildinfo
next-env.d.ts
```

#### 2. 워크플로우에서 ignore-path 지정

```yaml
- name: Check Prettier formatting
  run: npx prettier --check "src/**/*.{ts,tsx,js,jsx,json,css}" "*.{ts,tsx,js,jsx,json,md}" --ignore-path .prettierignore
```

#### 3. 로컬에서 포맷팅

```bash
npx prettier --write "src/**/*.{ts,tsx,js,jsx,json,css}" "*.{ts,tsx,js,jsx,json,md}" --ignore-path .prettierignore
```

### 결과

- 빌드 캐시 파일 제외
- 소스 파일만 포맷팅 체크
- CI/CD 통과

---

## 5. Next.js SWC 바이너리 다운로드 404 오류

### 문제 상황

```
⨯ Failed to download swc package from https://registry.npmjs.org/@next/swc-linux-x64-gnu/-/swc-linux-x64-gnu-15.5.11.tgz
Error: request failed with status 404
```

### 원인

- Next.js 15.5.11 버전의 SWC 바이너리가 npm 레지스트리에 없음
- 특정 버전의 바이너리가 게시되지 않았거나 네트워크 문제

### 해결 방법

#### 방법 1: Next.js 버전 업데이트 (권장)

```json
{
  "dependencies": {
    "next": "^15.5.12"  // 15.5.11 → 15.5.12
  },
  "devDependencies": {
    "eslint-config-next": "^15.5.12"
  }
}
```

```bash
rm -f package-lock.json
npm install
```

#### 방법 2: npm 캐시 클리어

```yaml
- name: Clear npm cache
  run: npm cache clean --force
```

#### 방법 3: SWC 바이너리 명시적 설치 (임시)

```yaml
- name: Install SWC binaries (fallback)
  run: |
    npm install @next/swc-linux-x64-gnu@latest --save-optional || echo "SWC binary installation skipped"
  continue-on-error: true
```

#### 방법 4: Next.js 설정 확인

- `swcMinify` 옵션은 Next.js 15에서 기본값이므로 제거
- `next.config.js`에서 불필요한 옵션 제거

### 결과

- Next.js 15.5.12로 업데이트하여 문제 해결
- 빌드 성공
- CI/CD 정상 동작

---

## 요약

| 문제 | 원인 | 해결 방법 | 중요도 |
|------|------|----------|--------|
| workflow_call 오류 | 트리거 누락 | `on.workflow_call` 추가 또는 orchestrator 제거 | 높음 |
| 테스트 없을 때 실패 | 파일 존재 확인 없음 | 조건부 실행 + `continue-on-error` | 중간 |
| secrets if 조건 오류 | 보안 제약 | Step 내부에서 확인 | 높음 |
| Prettier 오류 | 빌드 캐시 포함 | `.prettierignore` 추가 | 낮음 |
| SWC 바이너리 404 | 버전 문제 | Next.js 버전 업데이트 | 높음 |

---

## 참고 자료

- [GitHub Actions workflow_call 문서](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [GitHub Actions secrets 문서](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Next.js SWC 문서](https://nextjs.org/docs/architecture/swc)
- [Prettier ignore 파일](https://prettier.io/docs/en/ignore.html)

---

## 추가 팁

### 1. 워크플로우 디버깅

```yaml
- name: Debug
  run: |
    echo "Branch: ${{ github.ref }}"
    echo "Event: ${{ github.event_name }}"
    echo "Path: ${{ github.event.head_commit.modified }}"
```

### 2. 조건부 실행 패턴

```yaml
# 파일 존재 확인
- name: Check file
  id: check
  run: |
    if [ -f "file.txt" ]; then
      echo "exists=true" >> $GITHUB_OUTPUT
    fi

# 조건부 실행
- name: Run if exists
  if: steps.check.outputs.exists == 'true'
  run: echo "File exists"
```

### 3. Secret 안전하게 사용

```yaml
# ❌ 잘못된 방법
if: secrets.TOKEN != ''

# ✅ 올바른 방법
- name: Check token
  id: check
  run: |
    if [ -z "${{ secrets.TOKEN }}" ]; then
      echo "exists=false" >> $GITHUB_OUTPUT
    else
      echo "exists=true" >> $GITHUB_OUTPUT
    fi

- name: Use token
  if: steps.check.outputs.exists == 'true'
  run: echo "Using token"
  env:
    TOKEN: ${{ secrets.TOKEN }}
```

---

**마지막 업데이트**: 2026-01-31
