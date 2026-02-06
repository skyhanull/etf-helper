# CI/CD 템플릿 사용 가이드

이 가이드는 재사용 가능한 CI/CD 템플릿을 사용하여 새 프로젝트에 CI/CD를 빠르게 설정하는 방법을 설명합니다.

## 빠른 시작

### 1단계: 템플릿 복사

```bash
# 프론트엔드 워크플로우
cp .github/workflows/templates/frontend-template.yml .github/workflows/frontend.yml

# 백엔드 워크플로우
cp .github/workflows/templates/backend-template.yml .github/workflows/backend.yml

# Prettier 설정
cp .github/workflows/templates/.prettierignore.template frontend/.prettierignore

# Next.js 설정 (필요시)
cp .github/workflows/templates/next.config.template.js frontend/next.config.js
```

### 2단계: 프로젝트에 맞게 수정

#### 프론트엔드 워크플로우 수정

```yaml
# .github/workflows/frontend.yml

# 1. 작업 디렉토리 변경
defaults:
  run:
    working-directory: frontend  # 프로젝트 구조에 맞게 변경

# 2. 경로 필터 변경
paths:
  - 'frontend/**'  # 실제 프론트엔드 디렉토리 경로로 변경

# 3. Node.js 버전 변경
env:
  NODE_VERSION: '20'  # 원하는 버전으로 변경

# 4. 브랜치 이름 변경
branches: [main, develop]  # 프로젝트 브랜치로 변경
```

#### 백엔드 워크플로우 수정

```yaml
# .github/workflows/backend.yml

# 1. 작업 디렉토리 변경
defaults:
  run:
    working-directory: backend  # 프로젝트 구조에 맞게 변경

# 2. 경로 필터 변경
paths:
  - 'backend/**'  # 실제 백엔드 디렉토리 경로로 변경

# 3. Python 버전 변경
env:
  PYTHON_VERSION: '3.11'  # 원하는 버전으로 변경

# 4. 브랜치 이름 변경
branches: [main, develop]  # 프로젝트 브랜치로 변경
```

### 3단계: GitHub Secrets 설정

#### Vercel 배포 (프론트엔드)

1. Vercel Dashboard → Settings → Tokens
2. 토큰 생성
3. GitHub 저장소 → Settings → Secrets and variables → Actions
4. `VERCEL_TOKEN` 추가

#### Railway 배포 (백엔드)

1. Railway Dashboard → Settings → Tokens
2. 토큰 생성
3. GitHub 저장소 → Settings → Secrets and variables → Actions
4. `RAILWAY_TOKEN` 추가

#### Render 배포 (백엔드)

1. Render Dashboard → Webhook
2. Deploy Hook URL 생성
3. GitHub 저장소 → Settings → Secrets and variables → Actions
4. `RENDER_DEPLOY_HOOK_URL` 추가

## 상세 설정

### Monorepo 구조

Monorepo 구조에서 사용하는 경우:

```yaml
# 프론트엔드
paths:
  - 'apps/frontend/**'
  - '.github/workflows/frontend.yml'

defaults:
  run:
    working-directory: apps/frontend

# 백엔드
paths:
  - 'apps/backend/**'
  - '.github/workflows/backend.yml'

defaults:
  run:
    working-directory: apps/backend
```

### 단일 저장소 구조

단일 저장소에서 사용하는 경우:

```yaml
# 프론트엔드
paths:
  - 'src/**'
  - 'package.json'
  - '.github/workflows/frontend.yml'

defaults:
  run:
    working-directory: .  # 루트 디렉토리

# 백엔드
paths:
  - 'app/**'
  - 'requirements.txt'
  - '.github/workflows/backend.yml'

defaults:
  run:
    working-directory: .  # 루트 디렉토리
```

### 테스트 활성화

#### 프론트엔드 테스트

```yaml
# .github/workflows/frontend.yml에서 주석 해제
test:
  name: Test
  runs-on: ubuntu-latest
  defaults:
    run:
      working-directory: frontend
  needs: lint

  steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: ${{ env.NODE_VERSION }}
        cache: 'npm'

    - name: Install dependencies
      run: npm ci

    - name: Run tests
      run: npm run test
```

#### 백엔드 테스트

백엔드 템플릿은 이미 테스트가 활성화되어 있습니다. 테스트 파일을 추가하면 자동으로 실행됩니다.

### 커버리지 리포트

#### 프론트엔드

```yaml
- name: Upload coverage reports
  uses: codecov/codecov-action@v4
  with:
    files: ./frontend/coverage/lcov.info
    flags: frontend
    name: frontend-coverage
```

#### 백엔드

백엔드 템플릿에 이미 포함되어 있습니다.

## 문제 해결

### 일반적인 문제

1. **워크플로우가 실행되지 않음**
   - 경로 필터 확인
   - 브랜치 이름 확인
   - 파일 경로 확인

2. **빌드 실패**
   - 로컬에서 빌드 테스트
   - 의존성 버전 확인
   - 환경 변수 확인

3. **배포 실패**
   - Secret 설정 확인
   - 배포 플랫폼 설정 확인
   - 로그 확인

### 자세한 문제 해결

[CI_CD_TROUBLESHOOTING.md](./CI_CD_TROUBLESHOOTING.md)를 참고하세요.

## 체크리스트

### 초기 설정

- [ ] 템플릿 파일 복사
- [ ] 작업 디렉토리 수정
- [ ] 경로 필터 수정
- [ ] 브랜치 이름 수정
- [ ] 버전 설정 확인

### Secret 설정

- [ ] VERCEL_TOKEN 설정 (프론트엔드)
- [ ] RAILWAY_TOKEN 설정 (백엔드)
- [ ] RENDER_DEPLOY_HOOK_URL 설정 (백엔드, 선택)

### 테스트

- [ ] 로컬에서 빌드 테스트
- [ ] GitHub Actions에서 워크플로우 실행 확인
- [ ] 배포 테스트

## 예제 프로젝트 구조

```
project/
├── .github/
│   └── workflows/
│       ├── frontend.yml
│       └── backend.yml
├── frontend/
│   ├── .prettierignore
│   ├── next.config.js
│   ├── package.json
│   └── src/
└── backend/
    ├── requirements.txt
    ├── app/
    └── tests/
```

## 추가 리소스

- [GitHub Actions 공식 문서](https://docs.github.com/en/actions)
- [Vercel 배포 가이드](./VERCEL_DEPLOYMENT.md)
- [백엔드 배포 가이드](./BACKEND_DEPLOYMENT.md)
- [CI/CD 문제 해결 가이드](./CI_CD_TROUBLESHOOTING.md)

---

**마지막 업데이트**: 2026-01-31
