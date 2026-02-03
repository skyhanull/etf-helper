# CI/CD 파이프라인 가이드

## 개요

프로젝트에 GitHub Actions를 사용한 CI/CD 파이프라인이 구축되었습니다.

## 워크플로우 구조

```
.github/workflows/
├── ci.yml          # 전체 통합 파이프라인
├── frontend.yml    # 프론트엔드 전용 CI/CD
└── backend.yml     # 백엔드 전용 CI/CD
```

## 프론트엔드 CI/CD (`frontend.yml`)

### 트리거 조건
- `main`, `develop` 브랜치에 push
- `main`, `develop` 브랜치로 PR 생성
- `frontend/**` 경로 변경 시

### 실행 단계

#### 1. Lint & Type Check
- ESLint 실행
- TypeScript 타입 체크
- Prettier 포맷팅 검사

#### 2. Build
- Next.js 프로덕션 빌드
- 빌드 아티팩트 저장 (7일간 보관)

#### 3. Test (향후 활성화)
- 단위 테스트 실행
- 통합 테스트 실행

#### 4. Deploy (주석 처리됨)
- Vercel 배포 (선택)
- Railway 배포 (선택)

### 환경 변수
- `NEXT_PUBLIC_API_URL`: API 서버 URL (기본값: `http://localhost:8000`)

## 백엔드 CI/CD (`backend.yml`)

### 트리거 조건
- `main`, `develop` 브랜치에 push
- `main`, `develop` 브랜치로 PR 생성
- `backend/**` 경로 변경 시

### 실행 단계

#### 1. Lint & Format Check
- Ruff 린터 실행
- Ruff 포맷터 검사

#### 2. Test
- pytest 실행
- 테스트 커버리지 수집
- Codecov에 커버리지 업로드

#### 3. Migration Check
- PostgreSQL 서비스 컨테이너 실행
- Alembic 마이그레이션 검증

#### 4. Deploy (주석 처리됨)
- Railway 배포 (선택)
- Render 배포 (선택)

### 서비스
- **PostgreSQL 15**: 테스트용 데이터베이스

## 전체 통합 파이프라인 (`ci.yml`)

프론트엔드와 백엔드 CI/CD를 통합하여 실행합니다.

### 실행 순서
1. 프론트엔드 CI 실행
2. 백엔드 CI 실행
3. 통합 테스트 (향후 추가)

## GitHub Secrets 설정

배포를 활성화하려면 다음 Secrets를 설정해야 합니다:

### Vercel 배포 (프론트엔드)
```
VERCEL_TOKEN=your_vercel_token
VERCEL_ORG_ID=your_org_id
VERCEL_PROJECT_ID=your_project_id
```

### Railway 배포 (백엔드)
```
RAILWAY_TOKEN=your_railway_token
```

## 로컬에서 테스트

### 프론트엔드
```bash
cd frontend
npm ci
npm run lint
npm run type-check
npm run build
```

### 백엔드
```bash
cd backend
pip install -r requirements.txt
ruff check .
ruff format --check .
pytest
```

## CI/CD 상태 확인

GitHub Actions 탭에서 다음을 확인할 수 있습니다:
- 워크플로우 실행 상태
- 각 단계별 로그
- 빌드 아티팩트
- 테스트 커버리지

## 문제 해결

### 빌드 실패
1. 로컬에서 동일한 명령어 실행
2. 에러 로그 확인
3. 의존성 버전 확인

### 테스트 실패
1. 로컬에서 테스트 실행
2. 환경 변수 확인
3. 데이터베이스 연결 확인

### 배포 실패
1. Secrets 설정 확인
2. 배포 플랫폼 권한 확인
3. 빌드 로그 확인

## 향후 개선 사항

1. **자동 배포**
   - main 브랜치에 머지 시 자동 배포
   - Preview 배포 (PR별)

2. **성능 테스트**
   - Lighthouse CI
   - Bundle 크기 모니터링

3. **보안 스캔**
   - Dependabot
   - CodeQL

4. **알림 설정**
   - Slack/Discord 웹훅
   - 이메일 알림

## 참고 자료

- [GitHub Actions 문서](https://docs.github.com/en/actions)
- [Next.js 배포 가이드](https://nextjs.org/docs/deployment)
- [FastAPI 배포 가이드](https://fastapi.tiangolo.com/deployment/)
