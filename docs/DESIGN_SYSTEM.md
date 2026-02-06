# 디자인 시스템 가이드

이 문서는 프로젝트의 디자인 시스템을 설명합니다.

## 🎨 색상 팔레트

### 기본 색상

프로젝트에서 사용하는 주요 색상입니다.

#### Tailwind 클래스 사용법

```tsx
// Primary (파란색)
<div className="bg-primary-palette text-white">Primary</div>
<div className="text-primary-palette">Primary Text</div>

// Secondary (회색)
<div className="bg-secondary-palette text-white">Secondary</div>

// Success (초록색)
<div className="bg-success text-white">Success</div>
<div className="text-success">Success Text</div>

// Warning (노란색)
<div className="bg-warning text-white">Warning</div>
<div className="text-warning">Warning Text</div>

// Error (빨간색)
<div className="bg-error text-white">Error</div>
<div className="text-error">Error Text</div>
```

#### 직접 색상 값 사용

```tsx
// 인라인 스타일
<div style={{ color: '#3b82f6' }}>Primary</div>
<div style={{ backgroundColor: '#10b981' }}>Success</div>
```

### 색상 값

| 색상 | Hex 값 | Tailwind 클래스 | 용도 |
|------|--------|----------------|------|
| Primary | `#3b82f6` | `bg-primary-palette`, `text-primary-palette` | 주요 액션, 링크 |
| Secondary | `#6b7280` | `bg-secondary-palette`, `text-secondary-palette` | 보조 요소 |
| Success | `#10b981` | `bg-success`, `text-success` | 성공 메시지, 완료 상태 |
| Warning | `#f59e0b` | `bg-warning`, `text-warning` | 경고 메시지 |
| Error | `#ef4444` | `bg-error`, `text-error` | 에러 메시지, 삭제 액션 |

### 색상 변형

각 색상은 light/dark 변형도 제공됩니다.

```tsx
// Success 변형
<div className="bg-success-light">Light Success</div>
<div className="bg-success">Default Success</div>
<div className="bg-success-dark">Dark Success</div>
```

---

## 📏 간격 시스템

### 사용법

Tailwind의 spacing 유틸리티를 사용합니다.

```tsx
// 마진
<div className="m-1">4px margin</div>
<div className="m-2">8px margin</div>
<div className="m-3">12px margin</div>
<div className="m-4">16px margin</div>
<div className="m-6">24px margin</div>
<div className="m-8">32px margin</div>

// 패딩
<div className="p-1">4px padding</div>
<div className="p-2">8px padding</div>
<div className="p-4">16px padding</div>

// 간격 (gap)
<div className="flex gap-2">8px gap</div>
<div className="grid gap-4">16px gap</div>
```

### 간격 값

| 변수 | 값 | Tailwind 클래스 | 용도 |
|------|-----|----------------|------|
| `$1` | 4px | `1` | 매우 작은 간격 |
| `$2` | 8px | `2` | 작은 간격 |
| `$3` | 12px | `3` | 중간-작은 간격 |
| `$4` | 16px | `4` | 기본 간격 |
| `$6` | 24px | `6` | 중간 간격 |
| `$8` | 32px | `8` | 큰 간격 |

### 예시

```tsx
// 카드 레이아웃
<div className="p-4 gap-4">
  <div className="mb-2">Title</div>
  <div className="mb-4">Content</div>
</div>

// 버튼 그룹
<div className="flex gap-2">
  <button>Button 1</button>
  <button>Button 2</button>
</div>
```

---

## 📝 폰트 크기

### 사용법

Tailwind의 typography 유틸리티를 사용합니다.

```tsx
// 기본 사용
<p className="text-xs">12px 텍스트</p>
<p className="text-sm">14px 텍스트</p>
<p className="text-base">16px 텍스트</p>
<p className="text-lg">18px 텍스트</p>
<p className="text-xl">20px 텍스트</p>
<p className="text-2xl">24px 텍스트</p>
<p className="text-3xl">30px 텍스트</p>
<p className="text-4xl">36px 텍스트</p>
<p className="text-5xl">48px 텍스트</p>
```

### 폰트 크기 값

| 변수 | 값 | Tailwind 클래스 | 용도 |
|------|-----|----------------|------|
| `$xs` | 12px | `text-xs` | 작은 라벨, 캡션 |
| `$sm` | 14px | `text-sm` | 보조 텍스트 |
| `$base` | 16px | `text-base` | 기본 본문 텍스트 |
| `$lg` | 18px | `text-lg` | 강조 텍스트 |
| `$xl` | 20px | `text-xl` | 작은 제목 |
| `$2xl` | 24px | `text-2xl` | 중간 제목 |
| `$3xl` | 30px | `text-3xl` | 큰 제목 |
| `$4xl` | 36px | `text-4xl` | 매우 큰 제목 |
| `$5xl` | 48px | `text-5xl` | 히어로 제목 |

### 예시

```tsx
// 제목 계층
<h1 className="text-4xl font-bold">Main Title</h1>
<h2 className="text-2xl font-semibold">Section Title</h2>
<h3 className="text-xl font-medium">Subsection Title</h3>
<p className="text-base">Body text</p>
<span className="text-sm text-muted-foreground">Caption</span>
```

---

## 📱 반응형 디자인

### 브레이크포인트

프로젝트는 다음 브레이크포인트를 사용합니다.

| 디바이스 | 크기 | Tailwind 접두사 | 용도 |
|----------|------|----------------|------|
| Mobile | < 640px | 기본 (접두사 없음) | 모바일 화면 |
| Tablet | ≥ 640px | `sm:` | 태블릿 화면 |
| Desktop | ≥ 1024px | `lg:` | 데스크톱 화면 |

### 사용법

```tsx
// 모바일 우선 접근법
<div className="
  w-full          // 모바일: 전체 너비
  sm:w-1/2        // 태블릿: 절반 너비
  lg:w-1/3        // 데스크톱: 1/3 너비
">
  Responsive Container
</div>

// 그리드 레이아웃
<div className="
  grid grid-cols-1      // 모바일: 1열
  sm:grid-cols-2       // 태블릿: 2열
  lg:grid-cols-3       // 데스크톱: 3열
  gap-4
">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>

// 폰트 크기 조정
<h1 className="
  text-2xl        // 모바일: 24px
  sm:text-3xl     // 태블릿: 30px
  lg:text-4xl     // 데스크톱: 36px
">
  Responsive Title
</h1>
```

### 반응형 패턴 예시

```tsx
// 네비게이션 바
<nav className="
  flex flex-col          // 모바일: 세로 배치
  sm:flex-row           // 태블릿 이상: 가로 배치
  gap-2
  p-4                   // 모바일: 16px 패딩
  lg:p-6                // 데스크톱: 24px 패딩
">
  <a href="/">Home</a>
  <a href="/about">About</a>
</nav>

// 카드 그리드
<div className="
  grid
  grid-cols-1           // 모바일: 1열
  sm:grid-cols-2        // 태블릿: 2열
  lg:grid-cols-4        // 데스크톱: 4열
  gap-4
">
  {cards.map(card => <Card key={card.id} {...card} />)}
</div>
```

---

## 🎯 사용 예시

### 버튼 컴포넌트

```tsx
// Primary 버튼
<button className="
  bg-primary-palette
  text-white
  px-4 py-2
  rounded-lg
  text-base
  hover:bg-primary-palette/90
">
  Primary Button
</button>

// Success 버튼
<button className="
  bg-success
  text-white
  px-4 py-2
  rounded-lg
  text-base
">
  Success Button
</button>

// Error 버튼
<button className="
  bg-error
  text-white
  px-4 py-2
  rounded-lg
  text-base
">
  Delete
</button>
```

### 카드 컴포넌트

```tsx
<div className="
  bg-card
  border border-border
  rounded-lg
  p-4                    // $4 = 16px
  gap-4                  // $4 = 16px
">
  <h2 className="text-2xl font-semibold mb-2">Card Title</h2>
  <p className="text-base text-muted-foreground">
    Card content goes here
  </p>
</div>
```

### 폼 컴포넌트

```tsx
<div className="space-y-4">
  <div>
    <label className="text-sm font-medium mb-2 block">
      Email
    </label>
    <input
      type="email"
      className="
        w-full
        px-3 py-2
        border border-input
        rounded-md
        text-base
      "
    />
  </div>
  <button className="
    bg-primary-palette
    text-white
    px-4 py-2
    rounded-md
    text-base
  ">
    Submit
  </button>
</div>
```

---

## 🔧 커스터마이징

### 색상 추가

`tailwind.config.ts`에서 색상을 추가할 수 있습니다:

```typescript
colors: {
  custom: {
    DEFAULT: '#your-color',
    light: '#light-variant',
    dark: '#dark-variant',
  },
}
```

### 간격 추가

`tailwind.config.ts`에서 간격을 추가할 수 있습니다:

```typescript
spacing: {
  '10': '40px',
  '12': '48px',
}
```

### 폰트 크기 추가

`tailwind.config.ts`에서 폰트 크기를 추가할 수 있습니다:

```typescript
fontSize: {
  '6xl': '64px',
  '7xl': '72px',
}
```

---

## 📚 참고 자료

- [Tailwind CSS 문서](https://tailwindcss.com/docs)
- [shadcn/ui 디자인 시스템](https://ui.shadcn.com/)
- [디자인 토큰 가이드](https://www.designtokens.org/)

---

**마지막 업데이트**: 2026-01-31
