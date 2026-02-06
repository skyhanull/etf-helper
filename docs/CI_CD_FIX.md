# CI/CD 워크플로우 중복 실행 문제 해결

## 문제 원인

`ci.yml`이 `frontend.yml`과 `backend.yml`을 호출하는데, 각 워크플로우도 직접 실행되어 중복 실행되었습니다.

### 이전 구조 (문제)
```
push 이벤트 발생
├── ci.yml 실행 → frontend.yml 호출
├── ci.yml 실행 → backend.yml 호출
├── frontend.yml 직접 실행 (paths 필터)
└── backend.yml 직접 실행 (paths 필터)
```

→ 같은 작업이 여러 번 실행됨!

## 해결 방법

### 방법 1: ci.yml 삭제 (적용됨)

각 워크플로우가 독립적으로 실행되도록 `ci.yml`을 삭제했습니다.

### 현재 구조 (해결)
```
frontend/** 변경 시
└── frontend.yml만 실행

backend/** 변경 시
└── backend.yml만 실행
```

## 워크플로우 동작

### 프론트엔드 (`frontend.yml`)
- `frontend/**` 변경 시 자동 실행
- Lint → Build → Deploy to Vercel

### 백엔드 (`backend.yml`)
- `backend/**` 변경 시 자동 실행
- Lint → Test → Deploy to Railway/Render

## 통합 실행이 필요한 경우

나중에 통합 테스트가 필요하면:

```yaml
# .github/workflows/integration.yml
name: Integration Tests

on:
  workflow_dispatch:  # 수동 실행만

jobs:
  frontend:
    uses: ./.github/workflows/frontend.yml
    
  backend:
    uses: ./.github/workflows/backend.yml
    
  integration:
    needs: [frontend, backend]
    # 통합 테스트 실행
```

## 참고

- 각 워크플로우는 독립적으로 실행됩니다
- paths 필터로 불필요한 실행을 방지합니다
- 중복 실행 문제가 해결되었습니다
