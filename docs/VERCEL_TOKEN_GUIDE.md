# Vercel 토큰 발급 가이드

## 토큰 발급 위치

### 방법 1: 계정 설정에서
1. Vercel Dashboard 로그인
2. 우측 상단 프로필 아이콘 클릭
3. **Settings** 클릭
4. 왼쪽 메뉴에서 **Tokens** 클릭
5. "Create Token" 버튼 클릭

### 방법 2: 직접 URL 접근
https://vercel.com/account/tokens

### 방법 3: Vercel CLI로 확인
```bash
# Vercel CLI 설치 (없다면)
npm install -g vercel

# 로그인
vercel login

# 토큰 확인 (CLI가 자동으로 관리)
```

## 토큰 생성 단계

1. **Create Token** 클릭
2. 설정:
   - **Name**: `github-actions` (또는 원하는 이름)
   - **Expiration**: 원하는 기간 선택 (또는 "No expiration")
3. **Create Token** 클릭
4. **토큰 복사** (한 번만 보여줌!)

## GitHub Secrets에 추가

1. GitHub 저장소 → **Settings** → **Secrets and variables** → **Actions**
2. "New repository secret" 클릭
3. 추가:
   ```
   Name: VERCEL_TOKEN
   Value: [복사한 토큰]
   ```

## 대안: Vercel GitHub 통합 사용 (더 간단)

토큰 없이도 Vercel의 GitHub 통합을 사용할 수 있습니다:

1. Vercel Dashboard → **Add New Project**
2. GitHub 저장소 선택
3. Root Directory: `frontend` 설정
4. **Deploy** 클릭

→ 자동으로 GitHub와 연동되어 `main` 브랜치에 push 시 자동 배포됩니다!

## 참고

- 토큰은 GitHub Actions에서만 필요합니다
- Vercel의 GitHub 통합을 사용하면 토큰이 필요 없습니다
- 두 방법 모두 자동 배포가 가능합니다
