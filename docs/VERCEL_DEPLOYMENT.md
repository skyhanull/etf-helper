# Vercel + GitHub Actions CI/CD 설정 가이드

## 🎯 목표

GitHub Actions를 통해 자동으로 Vercel에 배포하는 CI/CD 파이프라인 구축

## 📋 설정 단계

### 1단계: Vercel 프로젝트 생성

#### 방법 1: Vercel 웹사이트에서 (초기 설정)

1. [Vercel](https://vercel.com)에 로그인
2. "Add New Project" 클릭
3. GitHub 저장소 선택
4. 프로젝트 설정:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build` (자동 감지)
   - **Output Directory**: `.next` (자동 감지)
5. **"Deploy"** 클릭 (일단 수동 배포로 프로젝트 생성)

#### 방법 2: Vercel CLI로 (선택)

```bash
cd frontend
npm install -g vercel
vercel login
vercel link  # 기존 프로젝트에 연결하거나 새 프로젝트 생성
```

### 2단계: Vercel 토큰 발급

1. Vercel Dashboard → [Settings](https://vercel.com/account/tokens) → **Tokens**
2. "Create Token" 클릭
3. 토큰 이름 입력 (예: `github-actions`)
4. Scope: **Full Account** 선택
5. "Create Token" 클릭
6. **토큰 복사** (한 번만 보여줌!)

### 3단계: GitHub Secrets 설정

1. GitHub 저장소로 이동
2. **Settings** → **Secrets and variables** → **Actions**
3. "New repository secret" 클릭
4. 다음 Secrets 추가:

#### 필수 Secrets

```
Name: VERCEL_TOKEN
Value: [2단계에서 복사한 토큰]
```

#### 선택적 Secrets

```
Name: NEXT_PUBLIC_API_URL
Value: https://your-api-domain.com  # 프로덕션 API URL
```

### 4단계: Vercel 프로젝트 정보 확인

Vercel 프로젝트의 Settings → General에서 확인:
- **Project ID**: `prj_xxxxx`
- **Organization ID**: `team_xxxxx` 또는 사용자 ID

(현재 설정에서는 이 정보가 필요 없지만, 참고용으로 확인)

### 5단계: GitHub Actions 워크플로우 확인

`.github/workflows/frontend.yml` 파일이 이미 설정되어 있습니다:

- ✅ **Lint & Type Check**: 코드 품질 검사
- ✅ **Build**: 프로덕션 빌드
- ✅ **Deploy (Production)**: `main` 브랜치에 push 시 자동 배포
- ✅ **Preview**: PR 생성 시 프리뷰 배포

## 🚀 사용 방법

### 자동 배포

#### Production 배포 (main 브랜치)

```bash
git checkout main
git add .
git commit -m "feat: 새로운 기능 추가"
git push origin main
```

→ 자동으로 Vercel에 배포됩니다!

#### Preview 배포 (Pull Request)

1. 새 브랜치 생성:
```bash
git checkout -b feature/new-feature
```

2. 변경사항 커밋:
```bash
git add .
git commit -m "feat: 새 기능"
git push origin feature/new-feature
```

3. GitHub에서 Pull Request 생성

→ 자동으로 Preview URL이 생성되고 PR에 댓글로 추가됩니다!

### 배포 상태 확인

1. **GitHub Actions**:
   - 저장소 → **Actions** 탭
   - 실행 중인 워크플로우 확인
   - "Deploy to Vercel" 단계 확인

2. **Vercel Dashboard**:
   - [Vercel Dashboard](https://vercel.com/dashboard)
   - 프로젝트 선택
   - Deployments 탭에서 배포 상태 확인

## 🔧 환경 변수 설정

### Vercel에서 환경 변수 설정

1. Vercel Dashboard → 프로젝트 → **Settings** → **Environment Variables**
2. 다음 변수 추가:

```
NEXT_PUBLIC_API_URL=https://your-api-domain.com
```

### GitHub Secrets로 설정 (CI/CD에서 사용)

GitHub Secrets에 설정하면 빌드 시 자동으로 주입됩니다:

```
NEXT_PUBLIC_API_URL=https://your-api-domain.com
```

## 📊 배포 워크플로우

### Production 배포 (main 브랜치)

```
코드 Push → Lint → Build → Deploy to Vercel (Production)
```

### Preview 배포 (Pull Request)

```
PR 생성 → Lint → Build → Deploy Preview → PR에 댓글 추가
```

## 🐛 문제 해결

### 배포가 실패하는 경우

#### 1. VERCEL_TOKEN 오류
```
Error: Vercel authentication error
```

**해결책:**
- GitHub Secrets에 `VERCEL_TOKEN`이 올바르게 설정되었는지 확인
- Vercel에서 새 토큰 발급 후 업데이트

#### 2. 프로젝트를 찾을 수 없음
```
Error: Project not found
```

**해결책:**
- `frontend/vercel.json` 파일 확인
- Vercel에서 프로젝트가 생성되었는지 확인
- `vercel link` 명령어로 프로젝트 연결

#### 3. 빌드 실패
```
Error: Build failed
```

**해결책:**
- 로컬에서 빌드 테스트:
  ```bash
  cd frontend
  npm run build
  ```
- 빌드 로그 확인 (GitHub Actions 또는 Vercel Dashboard)

#### 4. 환경 변수 누락
```
Error: Environment variable not found
```

**해결책:**
- Vercel Dashboard에서 환경 변수 설정
- GitHub Secrets에 환경 변수 추가

### 로컬에서 테스트

```bash
cd frontend

# Vercel CLI 설치
npm install -g vercel

# 로그인
vercel login

# 프로젝트 연결
vercel link

# 로컬 빌드 테스트
npm run build

# Vercel로 배포 테스트
vercel --prod
```

## 📝 커스터마이징

### 다른 브랜치도 배포하고 싶은 경우

`.github/workflows/frontend.yml` 파일 수정:

```yaml
if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/develop'
```

### 특정 경로 변경 시에만 배포

이미 설정되어 있습니다:
```yaml
paths:
  - 'frontend/**'
```

### 커스텀 도메인 설정

1. Vercel Dashboard → 프로젝트 → **Settings** → **Domains**
2. 도메인 추가
3. DNS 설정 (Vercel이 안내)

## ✅ 체크리스트

### 초기 설정
- [ ] Vercel 계정 생성 및 로그인
- [ ] Vercel 프로젝트 생성 (수동 배포 1회)
- [ ] Vercel 토큰 발급
- [ ] GitHub Secrets에 `VERCEL_TOKEN` 추가
- [ ] 환경 변수 설정 (필요시)

### 테스트
- [ ] `main` 브랜치에 push하여 배포 테스트
- [ ] PR 생성하여 Preview 배포 테스트
- [ ] 배포된 사이트 접속 확인

### 최적화 (선택)
- [ ] 커스텀 도메인 설정
- [ ] 환경 변수 최적화
- [ ] 빌드 캐시 설정

## 🎉 완료!

이제 코드를 push하면 자동으로 Vercel에 배포됩니다!

### 다음 단계

1. **백엔드 배포**: Railway, Render 등 설정
2. **모니터링**: Vercel Analytics 설정
3. **알림**: Slack/Discord 웹훅 설정

## 📚 참고 자료

- [Vercel 문서](https://vercel.com/docs)
- [Vercel CLI 문서](https://vercel.com/docs/cli)
- [GitHub Actions 문서](https://docs.github.com/en/actions)
- [Next.js 배포 가이드](https://nextjs.org/docs/deployment)

---

**문제가 있으면 GitHub Issues에 등록하세요!**
