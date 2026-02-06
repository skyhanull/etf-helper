# CI/CD 워크플로우 템플릿

이 디렉토리에는 재사용 가능한 CI/CD 워크플로우 템플릿이 포함되어 있습니다.

## 파일 구조

```
templates/
├── frontend-template.yml      # 프론트엔드 CI/CD 템플릿
├── backend-template.yml        # 백엔드 CI/CD 템플릿
├── .prettierignore.template   # Prettier ignore 템플릿
├── next.config.template.js     # Next.js 설정 템플릿
└── README.md                   # 이 파일
```

## 사용 방법

### 1. 프론트엔드 CI/CD 설정

```bash
# 템플릿을 워크플로우 디렉토리로 복사
cp .github/workflows/templates/frontend-template.yml .github/workflows/frontend.yml

# 프로젝트에 맞게 수정
# - working-directory 경로
# - Node.js 버전
# - 브랜치 이름
# - 경로 필터
```

### 2. 백엔드 CI/CD 설정

```bash
# 템플릿을 워크플로우 디렉토리로 복사
cp .github/workflows/templates/backend-template.yml .github/workflows/backend.yml

# 프로젝트에 맞게 수정
# - working-directory 경로
# - Python 버전
# - 브랜치 이름
# - 경로 필터
```

### 3. Prettier 설정

```bash
# 템플릿을 프로젝트 루트로 복사
cp .github/workflows/templates/.prettierignore.template frontend/.prettierignore

# 필요에 따라 수정
```

### 4. Next.js 설정

```bash
# 템플릿을 프로젝트로 복사
cp .github/workflows/templates/next.config.template.js frontend/next.config.js

# 프로젝트에 맞게 수정
```

## 주요 기능

### 프론트엔드 템플릿

- ✅ Lint & Type Check
- ✅ Build
- ✅ Vercel 배포 (Production)
- ✅ Vercel Preview 배포 (Pull Request)
- ✅ Secret 안전하게 처리
- ✅ npm 캐시 클리어
- ✅ SWC 바이너리 폴백

### 백엔드 템플릿

- ✅ Lint & Format Check (Ruff)
- ✅ Test (조건부 실행)
- ✅ Migration Check (조건부 실행)
- ✅ Railway 배포
- ✅ Render 배포
- ✅ Secret 안전하게 처리
- ✅ 테스트/마이그레이션 없을 때도 성공

## 커스터마이징

### 환경 변수 변경

```yaml
env:
  NODE_VERSION: '20'  # Node.js 버전
  PYTHON_VERSION: '3.11'  # Python 버전
```

### 브랜치 변경

```yaml
on:
  push:
    branches: [main, develop]  # 원하는 브랜치로 변경
```

### 경로 필터 변경

```yaml
paths:
  - 'frontend/**'  # 프로젝트 구조에 맞게 변경
```

## 문제 해결

자세한 문제 해결 가이드는 [CI_CD_TROUBLESHOOTING.md](../../docs/CI_CD_TROUBLESHOOTING.md)를 참고하세요.

## 참고 자료

- [GitHub Actions 문서](https://docs.github.com/en/actions)
- [Vercel 배포 가이드](../../docs/VERCEL_DEPLOYMENT.md)
- [백엔드 배포 가이드](../../docs/BACKEND_DEPLOYMENT.md)
- [CI/CD 문제 해결 가이드](../../docs/CI_CD_TROUBLESHOOTING.md)
