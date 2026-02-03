# ETF Helper 개발 컨벤션

## 1. 코딩 컨벤션

### 폴더/파일 네이밍

#### 프론트엔드 (Next.js App Router)

| 구분 | 규칙 | 예시 | 설명 |
|------|------|------|------|
| **폴더명** | kebab-case | `etf-detail/`, `api-client/`, `portfolio/` | 디렉토리 이름 |
| **페이지 파일** | `page.tsx` | `app/page.tsx`, `app/etfs/page.tsx` | Next.js App Router 규칙 (소문자 고정) |
| **레이아웃 파일** | `layout.tsx` | `app/layout.tsx` | Next.js App Router 규칙 (소문자 고정) |
| **컴포넌트 파일** | PascalCase | `EtfCard.tsx`, `PieChart.tsx`, `Button.tsx` | React 컴포넌트 (shadcn/ui는 소문자 허용) |
| **UI 컴포넌트** | kebab-case | `button.tsx`, `card.tsx`, `input.tsx` | shadcn/ui 컴포넌트 (소문자) |
| **훅 파일** | camelCase (use 접두사) | `useEtfList.ts`, `usePortfolio.ts`, `useApi.ts` | 커스텀 훅 |
| **유틸 파일** | camelCase | `format.ts`, `utils.ts`, `client.ts` | 유틸리티 함수 |
| **타입 파일** | `index.ts` 또는 `types.ts` | `types/index.ts`, `etf.types.ts` | 타입 정의 |
| **API 파일** | camelCase | `client.ts`, `etf.api.ts` | API 클라이언트 |
| **스토어 파일** | camelCase + .store | `portfolio.store.ts` | Zustand 스토어 |
| **Provider 파일** | PascalCase | `Providers.tsx` | Context Provider |

**실제 프로젝트 예시:**
```
frontend/src/
├── app/
│   ├── page.tsx              ✅ Next.js 페이지 (소문자 고정)
│   ├── layout.tsx            ✅ Next.js 레이아웃 (소문자 고정)
│   └── etfs/
│       └── page.tsx          ✅ Next.js 페이지 (소문자 고정)
├── components/
│   └── ui/
│       ├── button.tsx        ✅ shadcn/ui 컴포넌트 (소문자)
│       ├── card.tsx          ✅ shadcn/ui 컴포넌트 (소문자)
│       └── input.tsx         ✅ shadcn/ui 컴포넌트 (소문자)
├── lib/
│   ├── api/
│   │   └── client.ts         ✅ API 클라이언트 (소문자)
│   └── utils/
│       └── format.ts         ✅ 유틸리티 (소문자)
├── providers/
│   └── Providers.tsx         ✅ Provider (PascalCase)
└── types/
    └── index.ts              ✅ 타입 정의 (소문자)
```

#### 백엔드 (FastAPI)

| 구분 | 규칙 | 예시 | 설명 |
|------|------|------|------|
| **폴더명** | snake_case | `api/`, `core/`, `models/` | 디렉토리 이름 (소문자) |
| **모듈 파일** | snake_case | `etf.py`, `health.py`, `database.py` | Python 모듈 |
| **라우터 파일** | snake_case | `etf.py`, `portfolio.py` | API 라우터 |
| **서비스 파일** | snake_case + _service | `etf_service.py`, `portfolio_service.py` | 비즈니스 로직 |
| **리포지토리 파일** | snake_case + _repository | `etf_repository.py` | 데이터 접근 계층 |
| **모델 파일** | snake_case | `etf.py`, `portfolio.py` | SQLAlchemy 모델 |
| **스키마 파일** | snake_case | `response.py`, `request.py` | Pydantic 스키마 |
| **유틸 파일** | snake_case | `utils.py`, `helpers.py` | 유틸리티 함수 |
| **예외 파일** | snake_case | `exceptions.py` | 커스텀 예외 |
| **설정 파일** | snake_case | `config.py`, `database.py` | 설정 관리 |

**실제 프로젝트 예시:**
```
backend/app/
├── main.py                   ✅ FastAPI 앱 진입점
├── api/
│   └── routes/
│       ├── etf.py           ✅ ETF 라우터 (snake_case)
│       └── health.py         ✅ 헬스체크 라우터 (snake_case)
├── core/
│   ├── config.py            ✅ 설정 (snake_case)
│   ├── database.py          ✅ DB 연결 (snake_case)
│   └── exceptions.py        ✅ 예외 처리 (snake_case)
├── models/
│   └── etf.py               ✅ 데이터 모델 (snake_case)
└── schemas/
    └── response.py          ✅ 응답 스키마 (snake_case)
```

#### 파일 네이밍 규칙 요약

**프론트엔드:**
- Next.js 특수 파일: `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx` (소문자 고정)
- React 컴포넌트: PascalCase (예: `EtfCard.tsx`) 또는 kebab-case (shadcn/ui: `button.tsx`)
- 커스텀 훅: camelCase + `use` 접두사 (예: `useEtfList.ts`)
- 유틸리티: camelCase 또는 kebab-case (예: `format.ts`, `utils.ts`)

**백엔드:**
- 모든 파일: snake_case (예: `etf.py`, `etf_service.py`)
- 클래스: PascalCase (예: `class EtfService`)
- 함수/변수: snake_case (예: `def get_etf_list()`)

### 프론트엔드 (TypeScript/React)

```typescript
// 컴포넌트: PascalCase + 화살표 함수
export const EtfCard = ({ etf }: EtfCardProps) => {
  return <div>...</div>
}

// 훅: camelCase + use 접두사
export const useEtfList = () => { ... }

// 타입: PascalCase + interface 선호
interface EtfCardProps {
  etf: Etf
  onClick?: () => void
}

// 상수: SCREAMING_SNAKE_CASE
export const API_BASE_URL = 'https://api.example.com'
export const MAX_PAGE_SIZE = 20

// 함수: camelCase + 동사로 시작
const formatPrice = (price: number) => { ... }
const calculateReturn = (buy: number, current: number) => { ... }
```

### 백엔드 (Python/FastAPI)

```python
# 파일명: snake_case
# etf_router.py, portfolio_service.py

# 클래스: PascalCase
class EtfService:
    pass

# 함수/변수: snake_case
def get_etf_list(skip: int, limit: int):
    total_count = 0
    return {"items": [], "total": total_count}

# 상수: SCREAMING_SNAKE_CASE
MAX_PAGE_SIZE = 100
DATABASE_URL = "postgresql://..."

# Pydantic 모델: PascalCase
class EtfResponse(BaseModel):
    code: str
    name: str
    price: int
```

---

## 2. Git 규칙

### 브랜치 전략: GitHub Flow

```
main (배포용)
  │
  ├── feat/etf-list        # 기능 개발
  ├── feat/portfolio       # 기능 개발
  ├── fix/chart-bug        # 버그 수정
  ├── refactor/api-client  # 리팩토링
  └── docs/readme          # 문서
```

| 브랜치 타입 | 용도 | 예시 |
|-------------|------|------|
| `feat/` | 새 기능 | `feat/etf-search` |
| `fix/` | 버그 수정 | `fix/price-format` |
| `refactor/` | 리팩토링 | `refactor/api-hooks` |
| `docs/` | 문서 | `docs/api-spec` |
| `chore/` | 설정/기타 | `chore/eslint-setup` |

### 커밋 메시지: Conventional Commits

```
<type>(<scope>): <subject>

예시:
feat(etf): ETF 목록 API 연동
fix(portfolio): 수익률 계산 오류 수정
style(ui): EtfCard 패딩 조정
refactor(api): axios 인스턴스 분리
docs(readme): 설치 방법 추가
chore(deps): tanstack-query 업데이트
```

| Type | 설명 |
|------|------|
| `feat` | 새 기능 |
| `fix` | 버그 수정 |
| `style` | UI/CSS 변경 (로직 변경 X) |
| `refactor` | 리팩토링 |
| `docs` | 문서 |
| `chore` | 빌드, 설정, 의존성 |
| `test` | 테스트 |

---

## 3. 린터 & 포맷터 설정

### 프론트엔드

#### ESLint (`.eslintrc.json`)
```json
{
  "extends": [
    "next/core-web-vitals",
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended"
  ],
  "rules": {
    "@typescript-eslint/no-unused-vars": "warn",
    "@typescript-eslint/no-explicit-any": "warn",
    "prefer-const": "error",
    "no-console": ["warn", { "allow": ["warn", "error"] }]
  }
}
```

#### Prettier (`.prettierrc`)
```json
{
  "semi": false,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 100,
  "plugins": ["prettier-plugin-tailwindcss"]
}
```

### 백엔드

#### Ruff (`pyproject.toml`)
```toml
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "W", "F", "I", "B"]
ignore = ["E501"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

---

## 4. API 응답 포맷

### 표준 응답 구조

```typescript
// 성공 응답
{
  "success": true,
  "data": { ... },
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "totalPages": 8
  }
}

// 에러 응답
{
  "success": false,
  "error": {
    "code": "NOT_FOUND",
    "message": "ETF를 찾을 수 없습니다",
    "details": null
  }
}
```

### 에러 코드 정의

| 코드 | HTTP | 설명 |
|------|------|------|
| `BAD_REQUEST` | 400 | 잘못된 요청 파라미터 |
| `UNAUTHORIZED` | 401 | 인증 필요 |
| `FORBIDDEN` | 403 | 권한 없음 |
| `NOT_FOUND` | 404 | 리소스 없음 |
| `VALIDATION_ERROR` | 422 | 유효성 검사 실패 |
| `INTERNAL_ERROR` | 500 | 서버 내부 오류 |

---

## 5. 에러 핸들링 전략

### 백엔드 (FastAPI)

```python
# exceptions.py
class AppException(Exception):
    def __init__(self, code: str, message: str, status_code: int = 400):
        self.code = code
        self.message = message
        self.status_code = status_code

class NotFoundException(AppException):
    def __init__(self, message: str = "리소스를 찾을 수 없습니다"):
        super().__init__("NOT_FOUND", message, 404)

# main.py - 전역 에러 핸들러
@app.exception_handler(AppException)
async def app_exception_handler(request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {"code": exc.code, "message": exc.message}
        }
    )
```

### 프론트엔드 (React)

```typescript
// lib/api/client.ts
export const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
})

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    const errorData = error.response?.data?.error
    if (errorData) {
      toast.error(errorData.message)
    }
    return Promise.reject(error)
  }
)
```

---

## 6. 환경변수 관리

### 파일 구조

```
etf-helper/
├── frontend/
│   ├── .env.example          # 템플릿 (Git에 포함)
│   ├── .env.local            # 로컬 개발용 (Git 제외)
│   └── .env.production       # 프로덕션 (Git 제외)
│
└── backend/
    ├── .env.example
    ├── .env                  # 로컬 개발용 (Git 제외)
    └── .env.production       # 프로덕션 (Git 제외)
```

### 네이밍 규칙

```bash
# 프론트엔드 (.env.example)
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=ETF Helper

# 백엔드 (.env.example)
# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/etf_db

# External APIs
KIS_APP_KEY=your_app_key
KIS_APP_SECRET=your_app_secret

# App Config
DEBUG=true
LOG_LEVEL=INFO
```

---

## 7. 테스트 전략

### 테스트 피라미드

```
         /E2E\           적게 (핵심 플로우만)
        /─────\
       / 통합  \         중간 (API 연동)
      /─────────\
     /   단위    \       많이 (유틸, 훅, 서비스)
    /─────────────\
```

### MVP에서 테스트 범위

| 레이어 | 테스트 대상 | 도구 | 우선순위 |
|--------|------------|------|----------|
| **프론트 단위** | 유틸 함수, 커스텀 훅 | Vitest | 필수 |
| **백엔드 단위** | 서비스 로직, 유틸 | pytest | 필수 |
| **백엔드 통합** | API 엔드포인트 | pytest + httpx | 필수 |
| **프론트 통합** | 컴포넌트 렌더링 | React Testing Library | 나중에 |
| **E2E** | 핵심 사용자 플로우 | Playwright | 나중에 |

### 테스트 파일 위치

```
features/
├── etf/
│   ├── hooks/
│   │   └── useEtfList.ts
│   └── __tests__/
│       └── useEtfList.test.ts
```

---

## 8. 로깅 전략

### 로그 레벨

| 레벨 | 용도 | 예시 |
|------|------|------|
| `DEBUG` | 개발 디버깅용 | 변수 값, SQL 쿼리 |
| `INFO` | 일반 동작 기록 | API 요청, 작업 완료 |
| `WARNING` | 잠재적 문제 | 느린 쿼리, 재시도 |
| `ERROR` | 오류 발생 | 예외, 실패한 요청 |

### 로깅 규칙

```python
# 좋은 예
logger.info(f"ETF 조회 완료: code={code}, price={price}")
logger.error(f"KIS API 실패: status={status}, message={message}")

# 나쁜 예
logger.info("조회 완료")           # 정보 부족
logger.info(f"data={huge_object}") # 너무 많은 정보
print("디버깅...")                 # print 사용 금지
```

---

## 9. 보안 가이드라인

### 프론트엔드 보안

| 위협 | 대응 |
|------|------|
| **XSS** | React가 기본 이스케이프, `dangerouslySetInnerHTML` 금지 |
| **민감 정보 노출** | API 키는 서버에서만, `NEXT_PUBLIC_` 최소화 |

### 백엔드 보안

| 위협 | 대응 |
|------|------|
| **SQL Injection** | ORM 사용 (SQLAlchemy), raw SQL 금지 |
| **CORS** | 허용 도메인 명시적 설정 |
| **Rate Limiting** | slowapi로 API 남용 방지 |
| **입력 검증** | Pydantic으로 모든 입력 검증 |

### 보안 체크리스트

- [ ] 환경변수에 시크릿 저장 (.env)
- [ ] .env 파일 .gitignore에 포함
- [ ] CORS 허용 도메인 명시
- [ ] 모든 입력 데이터 검증 (Pydantic/Zod)
- [ ] SQL은 ORM으로만
- [ ] 에러 메시지에 내부 정보 노출 금지
- [ ] HTTPS 강제 (배포 환경)

---

## 10. 디자인 토큰

### 프로젝트 커스텀 토큰

```css
/* globals.css */
:root {
  /* 수익률 색상 */
  --profit: 142.1 76.2% 36.3%;      /* 초록 (상승) */
  --loss: 0 84.2% 60.2%;            /* 빨강 (하락) */

  /* 차트 색상 */
  --chart-1: 221.2 83.2% 53.3%;     /* 파랑 */
  --chart-2: 142.1 76.2% 36.3%;     /* 초록 */
  --chart-3: 47.9 95.8% 53.1%;      /* 노랑 */
  --chart-4: 280 65% 60%;           /* 보라 */
}
```

### Tailwind 설정

```typescript
// tailwind.config.ts
export default {
  theme: {
    extend: {
      colors: {
        profit: 'hsl(var(--profit))',
        loss: 'hsl(var(--loss))',
        chart: {
          1: 'hsl(var(--chart-1))',
          2: 'hsl(var(--chart-2))',
          3: 'hsl(var(--chart-3))',
          4: 'hsl(var(--chart-4))',
        },
      },
    },
  },
}
```

---

## 11. VS Code 설정

### `.vscode/settings.json`

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  },
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```

---

## 12. 기타 설정 파일

### `.gitignore`

```gitignore
# Dependencies
node_modules/
__pycache__/
*.pyc
.venv/

# Environment
.env
.env.local
.env.production

# Build
.next/
dist/

# IDE
.vscode/
.idea/

# OS
.DS_Store

# Database
*.db
*.sqlite

# Logs
*.log
```

### `.nvmrc`
```
20
```

### `.python-version`
```
3.11
```
