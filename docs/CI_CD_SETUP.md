# CI/CD 파이프라인 설정 가이드

## 🚀 빠른 시작

CI/CD 파이프라인은 이미 설정되어 있습니다! 코드를 GitHub에 push하면 자동으로 실행됩니다.

## 📋 현재 상태

### ✅ 이미 설정된 것들

1. **프론트엔드 CI/CD** (`.github/workflows/frontend.yml`)
   - ✅ Lint & Type Check
   - ✅ Build 검증
   - ⏸️ Test (주석 처리됨)
   - ⏸️ Deploy (주석 처리됨)

2. **백엔드 CI/CD** (`.github/workflows/backend.yml`)
   - ✅ Lint & Format Check
   - ✅ Test (pytest)
   - ✅ Migration Check (PostgreSQL)
   - ⏸️ Deploy (주석 처리됨)

3. **통합 파이프라인** (`.github/workflows/ci.yml`)
   - ✅ 프론트엔드 + 백엔드 동시 실행

## 🎯 지금 바로 사용하기

### 1단계: 코드 Push

```bash
git add .
git commit -m "feat: CI/CD 파이프라인 테스트"
git push origin main
```

### 2단계: GitHub에서 확인

1. GitHub 저장소로 이동
2. **Actions** 탭 클릭
3. 실행 중인 워크플로우 확인
4. 각 단계별 로그 확인

### 3단계: 결과 확인

- ✅ **초록색 체크**: 성공
- ❌ **빨간색 X**: 실패 (로그 확인 필요)
- 🟡 **노란색 원**: 실행 중

## 🔧 단계별 설정 가이드

### 1. 기본 CI (이미 작동 중)

현재 상태로도 다음이 자동 실행됩니다:

**프론트엔드:**
- ESLint 검사
- TypeScript 타입 체크
- Prettier 포맷팅 검사
- Next.js 빌드

**백엔드:**
- Ruff 린터 검사
- Ruff 포맷터 검사
- pytest 테스트 실행
- Alembic 마이그레이션 검증

### 2. 테스트 활성화 (선택)

#### 프론트엔드 테스트

1. 테스트 프레임워크 설치:
```bash
cd frontend
npm install --save-dev @testing-library/react @testing-library/jest-dom jest jest-environment-jsdom
```

2. `package.json`에 테스트 스크립트 추가:
```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch"
  }
}
```

3. `.github/workflows/frontend.yml`에서 테스트 섹션 주석 해제:
```yaml
- name: Test
  run: npm run test
```

#### 백엔드 테스트

이미 활성화되어 있습니다! 테스트 코드만 작성하면 됩니다.

### 3. 배포 설정 (선택)

#### Vercel 배포 (프론트엔드)

**방법 1: Vercel 웹사이트에서 설정 (추천)**
1. [Vercel](https://vercel.com)에 로그인
2. "Add New Project" 클릭
3. GitHub 저장소 선택
4. 프로젝트 설정:
   - Framework Preset: Next.js
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `.next`
5. Deploy 클릭

**방법 2: GitHub Actions로 배포**
1. Vercel 토큰 발급:
   - Vercel Dashboard → Settings → Tokens
   - 새 토큰 생성

2. GitHub Secrets 설정:
   - 저장소 → Settings → Secrets and variables → Actions
   - 다음 Secrets 추가:
     ```
     VERCEL_TOKEN=your_vercel_token
     VERCEL_ORG_ID=your_org_id
     VERCEL_PROJECT_ID=your_project_id
     ```

3. `.github/workflows/frontend.yml`에서 배포 섹션 주석 해제

#### Railway 배포 (백엔드)

**방법 1: Railway 웹사이트에서 설정 (추천)**
1. [Railway](https://railway.app)에 로그인
2. "New Project" 클릭
3. "Deploy from GitHub repo" 선택
4. 저장소 선택
5. 프로젝트 설정:
   - Root Directory: `backend`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. 환경 변수 설정 (`.env.example` 참고)

**방법 2: GitHub Actions로 배포**
1. Railway 토큰 발급:
   - Railway Dashboard → Account → Tokens
   - 새 토큰 생성

2. GitHub Secrets 설정:
   ```
   RAILWAY_TOKEN=your_railway_token
   ```

3. `.github/workflows/backend.yml`에서 배포 섹션 주석 해제

## 📊 CI/CD 동작 확인

### 로컬에서 테스트

**프론트엔드:**
```bash
cd frontend
npm ci                    # CI와 동일한 설치
npm run lint              # Lint 검사
npm run type-check        # TypeScript 검사
npm run build             # 빌드 테스트
```

**백엔드:**
```bash
cd backend
pip install -r requirements.txt
ruff check .              # Lint 검사
ruff format --check .     # 포맷 검사
pytest                    # 테스트 실행
```

### GitHub Actions에서 확인

1. **워크플로우 실행 확인**
   - 저장소 → Actions 탭
   - 최근 실행 목록 확인

2. **실패한 워크플로우 디버깅**
   - 실패한 워크플로우 클릭
   - 실패한 단계 클릭
   - 로그 확인

3. **빌드 아티팩트 확인**
   - 워크플로우 실행 페이지
   - "Artifacts" 섹션에서 다운로드

## 🐛 문제 해결

### CI가 실패하는 경우

#### 프론트엔드 빌드 실패
```bash
# 로컬에서 동일한 명령어 실행
cd frontend
npm ci
npm run build

# 에러 확인 후 수정
```

#### 백엔드 테스트 실패
```bash
# 로컬에서 테스트 실행
cd backend
pytest -v

# 에러 확인 후 수정
```

#### 타입 에러
```bash
# 프론트엔드
cd frontend
npm run type-check

# 에러 확인 후 수정
```

### 일반적인 문제

1. **의존성 버전 불일치**
   - `package-lock.json` 또는 `requirements.txt` 확인
   - 로컬과 CI 환경 동기화

2. **환경 변수 누락**
   - `.env.example` 확인
   - GitHub Secrets 설정 확인

3. **캐시 문제**
   - GitHub Actions 캐시 삭제
   - 로컬 `node_modules` 삭제 후 재설치

## 🎨 CI/CD 커스터마이징

### 브랜치 전략 변경

`.github/workflows/*.yml` 파일에서 `on.push.branches` 수정:

```yaml
on:
  push:
    branches: [main, develop, feature/*]  # 원하는 브랜치 추가
```

### 특정 경로 변경 시에만 실행

이미 설정되어 있습니다:
```yaml
paths:
  - 'frontend/**'  # frontend 폴더 변경 시에만 실행
```

### 추가 단계 추가

예: 코드 커버리지 리포트

```yaml
- name: Generate coverage report
  run: npm run test -- --coverage

- name: Upload coverage
  uses: codecov/codecov-action@v4
  with:
    files: ./coverage/lcov.info
```

## 📈 모니터링 및 알림

### GitHub Actions 알림

기본적으로 GitHub에서 이메일 알림을 보냅니다.

### Slack/Discord 알림 추가

1. 웹훅 URL 생성
2. GitHub Secrets에 추가:
   ```
   SLACK_WEBHOOK_URL=your_webhook_url
   ```
3. 워크플로우에 알림 단계 추가:
```yaml
- name: Notify Slack
  if: failure()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    webhook_url: ${{ secrets.SLACK_WEBHOOK_URL }}
```

## ✅ 체크리스트

### 기본 설정
- [x] GitHub Actions 워크플로우 파일 생성
- [x] 프론트엔드 CI 설정
- [x] 백엔드 CI 설정
- [ ] 코드 push하여 CI 실행 테스트

### 테스트 (선택)
- [ ] 프론트엔드 테스트 프레임워크 설치
- [ ] 테스트 코드 작성
- [ ] CI에서 테스트 실행 활성화

### 배포 (선택)
- [ ] 배포 플랫폼 선택 (Vercel/Railway 등)
- [ ] 배포 설정 완료
- [ ] GitHub Secrets 설정
- [ ] 자동 배포 테스트

## 🚀 다음 단계

1. **지금 바로**: 코드를 push하여 CI가 작동하는지 확인
2. **단기**: 테스트 코드 작성 후 CI에 통합
3. **중기**: 배포 플랫폼 설정 및 자동 배포 구축

## 📚 참고 자료

- [GitHub Actions 문서](https://docs.github.com/en/actions)
- [Next.js 배포 가이드](https://nextjs.org/docs/deployment)
- [FastAPI 배포 가이드](https://fastapi.tiangolo.com/deployment/)
- [Vercel 문서](https://vercel.com/docs)
- [Railway 문서](https://docs.railway.app)

---

**질문이나 문제가 있으면 GitHub Issues에 등록하세요!**
