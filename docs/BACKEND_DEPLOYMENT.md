# 백엔드 배포 가이드

## 🎯 배포 옵션

백엔드(FastAPI) 배포를 위한 여러 옵션이 있습니다:

1. **Railway** (추천) - 간단하고 무료 티어 제공
2. **Render** - 무료 티어 제공, GitHub 통합 쉬움
3. **Fly.io** - 무료 티어 제공, 전 세계 배포
4. **AWS/GCP/Azure** - 엔터프라이즈급 (복잡함)

## 🚀 Railway 배포 (추천)

### 1단계: Railway 프로젝트 생성

#### 방법 1: Railway 웹사이트에서 (추천)

1. [Railway](https://railway.app)에 로그인 (GitHub로 로그인)
2. "New Project" 클릭
3. "Deploy from GitHub repo" 선택
4. 저장소 선택
5. 프로젝트 설정:
   - **Root Directory**: `backend`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Build Command**: (비워두기 또는 `pip install -r requirements.txt`)

#### 방법 2: Railway CLI로

```bash
cd backend
npm install -g @railway/cli
railway login
railway init
railway up
```

### 2단계: 환경 변수 설정

Railway Dashboard → 프로젝트 → **Variables** 탭에서 추가:

```
DATABASE_URL=postgresql://user:pass@host:port/dbname
DEBUG=false
LOG_LEVEL=INFO
CORS_ORIGINS=https://your-frontend-domain.vercel.app
```

### 3단계: PostgreSQL 데이터베이스 추가

1. Railway Dashboard → 프로젝트 → "New" 클릭
2. "Database" → "Add PostgreSQL" 선택
3. 자동으로 `DATABASE_URL` 환경 변수가 생성됩니다

### 4단계: GitHub Actions 연동 (선택)

#### Railway 토큰 발급

1. Railway Dashboard → Account → **Tokens**
2. "New Token" 클릭
3. 토큰 복사

#### GitHub Secrets 설정

1. GitHub 저장소 → Settings → Secrets and variables → Actions
2. 추가:
   ```
   Name: RAILWAY_TOKEN
   Value: [Railway 토큰]
   ```

### 5단계: 테스트

```bash
git add .
git commit -m "feat: Railway 배포 설정"
git push origin main
```

→ Railway에서 자동 배포 확인!

---

## 🌐 Render 배포

### 1단계: Render 프로젝트 생성

1. [Render](https://render.com)에 로그인 (GitHub로 로그인)
2. "New +" → "Web Service" 클릭
3. GitHub 저장소 선택
4. 프로젝트 설정:
   - **Name**: `etf-helper-backend`
   - **Root Directory**: `backend`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### 2단계: 환경 변수 설정

Render Dashboard → 프로젝트 → **Environment** 탭에서 추가:

```
DATABASE_URL=postgresql://user:pass@host:port/dbname
DEBUG=false
LOG_LEVEL=INFO
CORS_ORIGINS=https://your-frontend-domain.vercel.app
```

### 3단계: PostgreSQL 데이터베이스 추가

1. Render Dashboard → "New +" → "PostgreSQL" 클릭
2. 데이터베이스 생성
3. **Internal Database URL** 복사하여 `DATABASE_URL`에 설정

### 4단계: 자동 배포 설정

Render는 GitHub와 자동 연동됩니다:
- `main` 브랜치에 push 시 자동 배포
- PR 생성 시 Preview 배포 (선택)

### 5단계: Webhook으로 GitHub Actions 연동 (선택)

1. Render Dashboard → 프로젝트 → **Settings** → **Webhooks**
2. "Add Webhook" 클릭
3. **Deploy Hook URL** 복사
4. GitHub Secrets에 추가:
   ```
   Name: RENDER_DEPLOY_HOOK_URL
   Value: [Deploy Hook URL]
   ```

---

## ✈️ Fly.io 배포

### 1단계: Fly.io CLI 설치 및 로그인

```bash
curl -L https://fly.io/install.sh | sh
fly auth login
```

### 2단계: 프로젝트 초기화

```bash
cd backend
fly launch
```

### 3단계: fly.toml 설정

`backend/fly.toml` 파일 생성:

```toml
app = "etf-helper-backend"
primary_region = "icn"

[build]

[env]
  PORT = "8080"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0
  processes = ["app"]

[[services]]
  protocol = "tcp"
  internal_port = 8080
  processes = ["app"]

  [[services.ports]]
    port = 80
    handlers = ["http"]
    force_https = true

  [[services.ports]]
    port = 443
    handlers = ["tls", "http"]
```

### 4단계: 배포

```bash
fly deploy
```

---

## 🔧 공통 설정

### CORS 설정 업데이트

프로덕션 환경에서는 프론트엔드 도메인을 명시해야 합니다:

```python
# backend/app/core/config.py
cors_origins: str = "https://your-app.vercel.app,https://www.your-domain.com"
```

### 환경 변수 체크리스트

필수 환경 변수:
- `DATABASE_URL` - PostgreSQL 연결 문자열
- `CORS_ORIGINS` - 프론트엔드 도메인 (쉼표로 구분)
- `DEBUG` - `false` (프로덕션)
- `LOG_LEVEL` - `INFO` 또는 `WARNING`

선택적 환경 변수:
- `KIS_APP_KEY` - 한국투자증권 API 키
- `KIS_APP_SECRET` - 한국투자증권 API 시크릿
- `SENTRY_DSN` - 에러 추적 (Sentry)

### 데이터베이스 마이그레이션

배포 후 마이그레이션 실행:

```bash
# Railway/Render/Fly.io에서 실행
alembic upgrade head
```

또는 배포 시 자동 실행하도록 설정:

```yaml
# Railway: railway.json에 추가
"deploy": {
  "startCommand": "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port $PORT"
}
```

---

## 📊 배포 플랫폼 비교

| 플랫폼 | 무료 티어 | 설정 난이도 | 추천도 |
|--------|----------|------------|--------|
| **Railway** | ✅ $5 크레딧/월 | ⭐ 쉬움 | ⭐⭐⭐⭐⭐ |
| **Render** | ✅ 무료 (제한적) | ⭐⭐ 쉬움 | ⭐⭐⭐⭐ |
| **Fly.io** | ✅ 무료 (제한적) | ⭐⭐⭐ 보통 | ⭐⭐⭐ |
| **AWS/GCP** | ⚠️ 제한적 | ⭐⭐⭐⭐⭐ 어려움 | ⭐⭐ |

---

## 🚀 빠른 시작: Railway (5분)

### 1. Railway 프로젝트 생성
- [railway.app](https://railway.app) → New Project → GitHub 저장소 선택

### 2. 환경 변수 설정
- `DATABASE_URL` (PostgreSQL 자동 생성)
- `CORS_ORIGINS` (프론트엔드 도메인)

### 3. GitHub Actions 연동 (선택)
- Railway 토큰 발급 → GitHub Secrets에 추가

### 4. 완료!
- `main` 브랜치에 push하면 자동 배포

---

## 🔗 프론트엔드와 연동

프론트엔드가 Vercel에 배포된 경우:

1. **백엔드 URL 확인**
   - Railway: 프로젝트 → Settings → Domains
   - Render: 프로젝트 → Settings → Custom Domain

2. **프론트엔드 환경 변수 업데이트**
   - Vercel Dashboard → 프로젝트 → Settings → Environment Variables
   - `NEXT_PUBLIC_API_URL=https://your-backend.railway.app`

3. **CORS 설정 확인**
   - 백엔드 `CORS_ORIGINS`에 프론트엔드 도메인 추가

---

## 🐛 문제 해결

### 배포 실패

**문제**: 빌드 실패
```bash
# 로컬에서 테스트
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**문제**: 데이터베이스 연결 실패
- `DATABASE_URL` 환경 변수 확인
- PostgreSQL 서비스가 실행 중인지 확인

**문제**: CORS 에러
- 백엔드 `CORS_ORIGINS`에 프론트엔드 도메인 추가
- 프론트엔드 `NEXT_PUBLIC_API_URL` 확인

---

## ✅ 체크리스트

### Railway 배포
- [ ] Railway 계정 생성
- [ ] 프로젝트 생성 (GitHub 연동)
- [ ] PostgreSQL 데이터베이스 추가
- [ ] 환경 변수 설정
- [ ] Railway 토큰 발급 (GitHub Actions용)
- [ ] GitHub Secrets 설정
- [ ] 배포 테스트

### Render 배포
- [ ] Render 계정 생성
- [ ] Web Service 생성
- [ ] PostgreSQL 데이터베이스 추가
- [ ] 환경 변수 설정
- [ ] Deploy Hook 생성 (선택)
- [ ] 배포 테스트

---

## 📚 참고 자료

- [Railway 문서](https://docs.railway.app)
- [Render 문서](https://render.com/docs)
- [Fly.io 문서](https://fly.io/docs)
- [FastAPI 배포 가이드](https://fastapi.tiangolo.com/deployment/)

---

**추천: Railway가 가장 간단하고 빠르게 시작할 수 있습니다!**
