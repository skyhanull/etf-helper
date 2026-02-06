# ETF Helper

국내 ETF 정보 조회, 비교, 포트폴리오 관리 서비스

## 프로젝트 구조

```
etf-helper/
├── frontend/          # Next.js 프론트엔드
├── backend/           # FastAPI 백엔드
├── docs/              # 기획서 및 문서
└── .github/           # GitHub Actions, 템플릿
```

## 시작하기

### Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

→ http://localhost:3000

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

→ http://localhost:8000
→ API 문서: http://localhost:8000/docs

## 기술 스택

### Frontend
- Next.js 15 (App Router)
- React 19
- TypeScript
- Tailwind CSS
- Tanstack Query
- Zustand

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- pykrx

## 배포

### Frontend
- **Vercel** - 자동 배포 (GitHub Actions)
- `main` 브랜치에 push 시 자동 배포
- Pull Request 시 Preview 배포

### Backend
- **Railway** 또는 **Render** (추천: Railway)
- GitHub Actions로 자동 배포 가능
- 자세한 내용: [백엔드 배포 가이드](./docs/BACKEND_DEPLOYMENT.md)

## 문서

### 프로젝트 문서
- [기획서](./docs/PLANNING.md)
- [개발 컨벤션](./docs/CONVENTIONS.md)
- [작업 계획](./docs/WORKPLAN.md)

### CI/CD 문서
- [CI/CD 문제 해결 가이드](./docs/CI_CD_TROUBLESHOOTING.md) - 발생한 문제와 해결 방법
- [CI/CD 템플릿 사용 가이드](./docs/CI_CD_TEMPLATE_GUIDE.md) - 재사용 가능한 템플릿 사용법
- [Vercel 배포 가이드](./docs/VERCEL_DEPLOYMENT.md)
- [백엔드 배포 가이드](./docs/BACKEND_DEPLOYMENT.md)

### CI/CD 템플릿
- [템플릿 디렉토리](./.github/workflows/templates/) - 재사용 가능한 워크플로우 템플릿
