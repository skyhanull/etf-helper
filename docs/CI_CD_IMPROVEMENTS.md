# CI/CD 개선 사항 가이드

현재 프로젝트의 CI/CD 설정을 개선할 수 있는 추가 사항들을 정리했습니다.

## 현재 상태 ✅

- ✅ 프론트엔드 CI/CD (Lint, Build, Deploy)
- ✅ 백엔드 CI/CD (Lint, Test, Deploy)
- ✅ 조건부 실행 (테스트/마이그레이션 없을 때 스킵)
- ✅ Secret 안전하게 처리
- ✅ Prettier 설정
- ✅ SWC 바이너리 폴백

## 추가 가능한 개선 사항

### 🔴 높은 우선순위 (즉시 추가 권장)

#### 1. Dependabot 설정 (보안 취약점 자동 업데이트)

**목적**: 의존성 패키지의 보안 취약점 자동 감지 및 업데이트

**파일**: `.github/dependabot.yml`

```yaml
version: 2
updates:
  # npm 패키지 (프론트엔드)
  - package-ecosystem: "npm"
    directory: "/frontend"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    labels:
      - "dependencies"
      - "frontend"

  # pip 패키지 (백엔드)
  - package-ecosystem: "pip"
    directory: "/backend"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    labels:
      - "dependencies"
      - "backend"
```

**장점**:
- 보안 취약점 자동 감지
- 의존성 자동 업데이트 PR 생성
- 보안 강화

---

#### 2. 워크플로우 상태 뱃지 (README에 표시)

**목적**: README에 CI/CD 상태를 시각적으로 표시

**README.md에 추가**:

```markdown
## CI/CD Status

![Frontend CI/CD](https://github.com/skyhanull/etf-helper/actions/workflows/frontend.yml/badge.svg)
![Backend CI/CD](https://github.com/skyhanull/etf-helper/actions/workflows/backend.yml/badge.svg)
```

**장점**:
- 프로젝트 상태를 한눈에 확인
- 신뢰도 향상

---

#### 3. 환경 변수 검증

**목적**: 배포 전 필수 환경 변수 확인

**프론트엔드 워크플로우에 추가**:

```yaml
- name: Validate environment variables
  run: |
    if [ -z "${{ secrets.NEXT_PUBLIC_API_URL }}" ]; then
      echo "⚠️ NEXT_PUBLIC_API_URL이 설정되지 않았습니다."
      echo "기본값(http://localhost:8000)을 사용합니다."
    else
      echo "✅ NEXT_PUBLIC_API_URL이 설정되어 있습니다."
    fi
```

**장점**:
- 배포 전 환경 변수 확인
- 문제 조기 발견

---

### 🟡 중간 우선순위 (추가하면 좋음)

#### 4. 빌드 시간 추적

**목적**: 빌드 시간 모니터링 및 최적화

**워크플로우에 추가**:

```yaml
- name: Build with timing
  run: |
    start_time=$(date +%s)
    npm run build
    end_time=$(date +%s)
    duration=$((end_time - start_time))
    echo "Build time: ${duration} seconds"
```

**장점**:
- 빌드 성능 모니터링
- 느려진 빌드 조기 발견

---

#### 5. 코드 커버리지 뱃지

**목적**: README에 테스트 커버리지 표시

**Codecov 설정 후 README에 추가**:

```markdown
![Codecov](https://codecov.io/gh/skyhanull/etf-helper/branch/main/graph/badge.svg)
```

**장점**:
- 테스트 커버리지 시각화
- 코드 품질 향상 동기

---

#### 6. 배포 알림 (선택사항)

**목적**: 배포 성공/실패 시 알림

**Slack 알림 예시**:

```yaml
- name: Notify Slack
  if: always()
  uses: slackapi/slack-github-action@v1
  with:
    webhook-url: ${{ secrets.SLACK_WEBHOOK_URL }}
    payload: |
      {
        "text": "Deployment ${{ job.status }}: ${{ github.ref }}"
      }
```

**장점**:
- 실시간 배포 상태 알림
- 문제 빠른 대응

---

### 🟢 낮은 우선순위 (나중에 추가 가능)

#### 7. 자동화된 이슈 생성

**목적**: CI/CD 실패 시 자동으로 이슈 생성

**워크플로우에 추가**:

```yaml
- name: Create issue on failure
  if: failure()
  uses: actions/github-script@v7
  with:
    script: |
      github.rest.issues.create({
        owner: context.repo.owner,
        repo: context.repo.repo,
        title: `CI/CD Failed: ${context.workflow}`,
        body: `Workflow failed: ${context.serverUrl}/${context.repo.owner}/${context.repo.repo}/actions/runs/${context.runId}`,
        labels: ['bug', 'ci/cd']
      })
```

**장점**:
- 실패 추적 자동화
- 문제 해결 추적

---

#### 8. 성능 벤치마크

**목적**: 빌드/테스트 성능 추적

**워크플로우에 추가**:

```yaml
- name: Performance benchmark
  run: |
    echo "## Performance Report" >> $GITHUB_STEP_SUMMARY
    echo "- Build time: $(date)" >> $GITHUB_STEP_SUMMARY
```

**장점**:
- 성능 추세 모니터링
- 최적화 포인트 발견

---

#### 9. 배포 롤백 자동화

**목적**: 배포 실패 시 자동 롤백

**Vercel/Railway에서 설정**:
- 자동 롤백 옵션 활성화
- 헬스 체크 설정

**장점**:
- 서비스 안정성 향상
- 빠른 복구

---

## 구현 가이드

### 1. Dependabot 설정

**파일 생성**: `.github/dependabot.yml`

```bash
mkdir -p .github
cat > .github/dependabot.yml << 'EOF'
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/frontend"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    labels:
      - "dependencies"
      - "frontend"

  - package-ecosystem: "pip"
    directory: "/backend"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    labels:
      - "dependencies"
      - "backend"
EOF
```

### 2. README에 뱃지 추가

**README.md 수정**:

```markdown
# ETF Helper

![Frontend CI/CD](https://github.com/skyhanull/etf-helper/actions/workflows/frontend.yml/badge.svg)
![Backend CI/CD](https://github.com/skyhanull/etf-helper/actions/workflows/backend.yml/badge.svg)

...
```

### 3. 환경 변수 검증 추가

**워크플로우에 step 추가**:

```yaml
- name: Validate environment variables
  run: |
    echo "Checking environment variables..."
    # 필수 변수 확인
    if [ -z "${{ secrets.NEXT_PUBLIC_API_URL }}" ]; then
      echo "⚠️ NEXT_PUBLIC_API_URL not set, using default"
    fi
```

## 우선순위별 체크리스트

### 즉시 추가 (🔴)

- [ ] Dependabot 설정
- [ ] 워크플로우 상태 뱃지
- [ ] 환경 변수 검증

### 추가하면 좋음 (🟡)

- [ ] 빌드 시간 추적
- [ ] 코드 커버리지 뱃지
- [ ] 배포 알림 (선택)

### 나중에 추가 (🟢)

- [ ] 자동화된 이슈 생성
- [ ] 성능 벤치마크
- [ ] 배포 롤백 자동화

## 참고 자료

- [Dependabot 문서](https://docs.github.com/en/code-security/dependabot)
- [GitHub Actions 뱃지](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)
- [Codecov 설정](https://docs.codecov.com/docs)

---

**마지막 업데이트**: 2026-01-31
