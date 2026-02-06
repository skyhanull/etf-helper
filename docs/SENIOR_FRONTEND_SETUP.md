# 시니어 프론트엔드 개발자를 위한 CI/CD 설정 가이드

프로덕션 레벨에서 시니어 프론트엔드 개발자들이 일반적으로 설정하는 CI/CD 개선 사항들을 정리했습니다.

## 현재 구현된 것 ✅

- ✅ 빌드 시간 추적
- ✅ Lint & Type Check
- ✅ Prettier 포맷팅
- ✅ 환경 변수 검증

## 추가 가능한 설정들

### 🔴 필수 (프로덕션 필수)

#### 1. Bundle Size 분석 및 제한

**목적**: 번들 크기를 모니터링하고 제한하여 성능 유지

**설치**:
```bash
cd frontend
npm install --save-dev @next/bundle-analyzer
```

**next.config.js 수정**:
```javascript
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
})

module.exports = withBundleAnalyzer({
  // 기존 설정...
})
```

**package.json 스크립트 추가**:
```json
{
  "scripts": {
    "analyze": "ANALYZE=true npm run build"
  }
}
```

**워크플로우에 추가**:
```yaml
- name: Analyze bundle size
  run: npm run analyze
  continue-on-error: true
```

**장점**:
- 번들 크기 모니터링
- 큰 의존성 조기 발견
- 성능 최적화 포인트 파악

---

#### 2. Bundle Size 제한 (size-limit)

**목적**: 번들 크기가 일정 크기를 넘지 않도록 제한

**설치**:
```bash
npm install --save-dev size-limit @size-limit/preset-next
```

**package.json 설정**:
```json
{
  "size-limit": [
    {
      "path": ".next/static/chunks/*.js",
      "limit": "200 KB"
    }
  ]
}
```

**워크플로우에 추가**:
```yaml
- name: Check bundle size
  run: npx size-limit
```

**장점**:
- 번들 크기 자동 검증
- 크기 증가 시 CI 실패
- 성능 저하 방지

---

#### 3. 보안 스캔 (npm audit)

**목적**: 보안 취약점 자동 감지

**워크플로우에 추가**:
```yaml
- name: Run security audit
  run: npm audit --audit-level=moderate
  continue-on-error: true
```

**장점**:
- 보안 취약점 자동 감지
- Dependabot과 함께 이중 보안

---

### 🟡 권장 (성능 모니터링)

#### 4. Lighthouse CI (성능 측정)

**목적**: 웹 성능 자동 측정 및 리포트

**설치**:
```bash
npm install --save-dev @lhci/cli
```

**lighthouserc.js 생성**:
```javascript
module.exports = {
  ci: {
    collect: {
      url: ['http://localhost:3000'],
      startServerCommand: 'npm run start',
      startServerReadyPattern: 'ready on',
      numberOfRuns: 3,
    },
    assert: {
      assertions: {
        'categories:performance': ['error', { minScore: 0.8 }],
        'categories:accessibility': ['error', { minScore: 0.9 }],
        'categories:best-practices': ['error', { minScore: 0.9 }],
        'categories:seo': ['error', { minScore: 0.9 }],
      },
    },
    upload: {
      target: 'temporary-public-storage',
    },
  },
}
```

**워크플로우에 추가**:
```yaml
- name: Run Lighthouse CI
  run: |
    npm run build
    npm run start &
    sleep 10
    npx lhci autorun
```

**장점**:
- 성능 점수 자동 측정
- 성능 저하 조기 발견
- SEO, 접근성 자동 검증

---

#### 5. Visual Regression Testing

**목적**: UI 변경사항 자동 감지

**도구**: Chromatic, Percy, 또는 Playwright

**예시 (Playwright)**:
```yaml
- name: Visual regression test
  run: |
    npm install -g @playwright/test
    npx playwright test --update-snapshots
```

**장점**:
- 의도치 않은 UI 변경 감지
- 디자인 일관성 유지

---

### 🟢 선택사항 (고급)

#### 6. E2E 테스트 (Playwright/Cypress)

**목적**: 실제 사용자 시나리오 테스트

**설치**:
```bash
npm install --save-dev @playwright/test
```

**워크플로우에 추가**:
```yaml
- name: Run E2E tests
  run: npx playwright test
```

**장점**:
- 실제 사용자 플로우 검증
- 통합 테스트

---

#### 7. 성능 메트릭 추적

**목적**: 실제 사용자 성능 데이터 수집

**도구**: Vercel Analytics, Google Analytics, 또는 Custom

**설치**:
```bash
npm install @vercel/analytics
```

**장점**:
- 실제 사용자 성능 모니터링
- 문제 조기 발견

---

#### 8. 에러 트래킹 (Sentry)

**목적**: 프로덕션 에러 자동 수집 및 알림

**설치**:
```bash
npm install @sentry/nextjs
```

**장점**:
- 프로덕션 에러 자동 수집
- 에러 발생 시 즉시 알림
- 스택 트레이스 자동 수집

---

## 구현 우선순위

### 즉시 구현 (필수)

1. ✅ 빌드 시간 추적 (완료)
2. Bundle Size 분석
3. Bundle Size 제한
4. 보안 스캔 (npm audit)

### 단기 구현 (권장)

5. Lighthouse CI
6. Visual Regression Testing

### 장기 구현 (선택)

7. E2E 테스트
8. 성능 메트릭 추적
9. 에러 트래킹

---

## 실제 구현 예시

### Bundle Size 분석 추가

**워크플로우에 추가**:
```yaml
- name: Analyze bundle size
  if: github.event_name == 'pull_request'
  run: |
    npm run build
    npm run analyze || echo "Bundle analyzer skipped"
  continue-on-error: true
```

### 보안 스캔 추가

**워크플로우에 추가**:
```yaml
- name: Security audit
  run: |
    echo "🔒 Running security audit..."
    npm audit --audit-level=moderate || echo "⚠️ Security vulnerabilities found"
  continue-on-error: true
```

---

## 체크리스트

### 필수 설정

- [x] 빌드 시간 추적
- [ ] Bundle Size 분석
- [ ] Bundle Size 제한
- [ ] 보안 스캔 (npm audit)

### 권장 설정

- [ ] Lighthouse CI
- [ ] Visual Regression Testing

### 선택 설정

- [ ] E2E 테스트
- [ ] 성능 메트릭 추적
- [ ] 에러 트래킹 (Sentry)

---

## 참고 자료

- [Next.js Bundle Analyzer](https://www.npmjs.com/package/@next/bundle-analyzer)
- [Size Limit](https://github.com/ai/size-limit)
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)
- [Playwright](https://playwright.dev/)
- [Sentry Next.js](https://docs.sentry.io/platforms/javascript/guides/nextjs/)

---

**마지막 업데이트**: 2026-01-31
