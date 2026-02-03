# 에러 바운더리 가이드

## 개요

프로젝트에 에러 바운더리(Error Boundary)가 추가되었습니다. 이는 React 애플리케이션에서 발생하는 JavaScript 에러를 캐치하고 처리하는 컴포넌트입니다.

## 구현된 에러 바운더리

### 1. `ErrorBoundary` 컴포넌트
**위치**: `src/components/ErrorBoundary.tsx`

클래스 컴포넌트 기반의 에러 바운더리입니다. 자식 컴포넌트 트리에서 발생하는 에러를 캐치합니다.

**사용 예시:**
```tsx
import { ErrorBoundary } from '@/components/ErrorBoundary'

function App() {
  return (
    <ErrorBoundary>
      <YourComponent />
    </ErrorBoundary>
  )
}
```

**커스텀 fallback:**
```tsx
<ErrorBoundary fallback={<CustomErrorUI />}>
  <YourComponent />
</ErrorBoundary>
```

### 2. Next.js App Router `error.tsx`
**위치**: `src/app/error.tsx`

Next.js App Router의 에러 페이지입니다. 서버 컴포넌트나 클라이언트 컴포넌트에서 발생하는 에러를 처리합니다.

**자동 적용**: Next.js가 자동으로 감지하여 사용합니다.

### 3. 루트 레이아웃에 적용
**위치**: `src/app/layout.tsx`

전역 에러 바운더리가 루트 레이아웃에 적용되어 있습니다.

## 기능

### 에러 바운더리 기능
- ✅ 에러 캐치 및 표시
- ✅ 개발 모드에서 상세 에러 정보 표시
- ✅ "다시 시도" 버튼 (에러 상태 리셋)
- ✅ "페이지 새로고침" 버튼
- ✅ 에러 로깅 (콘솔, 향후 Sentry 연동 가능)

### 개발 모드 vs 프로덕션 모드
- **개발 모드**: 에러 메시지와 스택 트레이스 표시
- **프로덕션 모드**: 사용자 친화적인 에러 메시지만 표시

## 사용 방법

### 기본 사용
```tsx
import { ErrorBoundary } from '@/components/ErrorBoundary'

export default function Page() {
  return (
    <ErrorBoundary>
      <YourComponent />
    </ErrorBoundary>
  )
}
```

### HOC 패턴 사용
```tsx
import { withErrorBoundary } from '@/components/ErrorBoundary'

const SafeComponent = withErrorBoundary(YourComponent)
```

### 특정 컴포넌트만 보호
```tsx
function Page() {
  return (
    <div>
      <SafeComponent />
      <ErrorBoundary>
        <RiskyComponent />
      </ErrorBoundary>
    </div>
  )
}
```

## 에러 바운더리가 캐치하지 않는 것

다음은 에러 바운더리가 캐치하지 **않습니다**:

1. **이벤트 핸들러 내부 에러**
   ```tsx
   // ❌ 에러 바운더리가 캐치하지 않음
   <button onClick={() => {
     throw new Error('이벤트 핸들러 에러')
   }}>Click</button>
   
   // ✅ try-catch로 처리
   <button onClick={() => {
     try {
       riskyOperation()
     } catch (error) {
       console.error(error)
     }
   }}>Click</button>
   ```

2. **비동기 코드 에러**
   ```tsx
   // ❌ 에러 바운더리가 캐치하지 않음
   useEffect(() => {
     fetch('/api/data')
       .then(() => {
         throw new Error('비동기 에러')
       })
   }, [])
   
   // ✅ .catch()로 처리
   useEffect(() => {
     fetch('/api/data')
       .catch(error => {
         console.error(error)
       })
   }, [])
   ```

3. **서버 컴포넌트 에러**
   - Next.js의 `error.tsx`가 처리합니다.

## 향후 개선 사항

1. **Sentry 연동**
   ```tsx
   componentDidCatch(error: Error, errorInfo: ErrorInfo) {
     Sentry.captureException(error, { extra: errorInfo })
   }
   ```

2. **에러 타입별 처리**
   - 네트워크 에러
   - 인증 에러
   - 데이터 검증 에러

3. **에러 리포팅 대시보드**
   - 에러 발생 빈도 추적
   - 사용자 영향도 분석

## 참고 자료

- [React Error Boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary)
- [Next.js Error Handling](https://nextjs.org/docs/app/api-reference/file-conventions/error)
