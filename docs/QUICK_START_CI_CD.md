# 🚀 빠른 시작: Vercel + GitHub Actions CI/CD

## 5분 안에 설정하기

### 1️⃣ Vercel 프로젝트 생성 (2분)

1. [vercel.com](https://vercel.com) 로그인
2. "Add New Project" → GitHub 저장소 선택
3. 설정:
   - Root Directory: `frontend`
   - Framework: Next.js (자동 감지)
4. **"Deploy"** 클릭 (일단 수동 배포)

### 2️⃣ Vercel 토큰 발급 (1분)

1. [Vercel Settings → Tokens](https://vercel.com/account/tokens)
2. "Create Token" 클릭
3. 이름 입력 → "Create Token"
4. **토큰 복사** (중요!)

### 3️⃣ GitHub Secrets 설정 (1분)

1. GitHub 저장소 → **Settings** → **Secrets and variables** → **Actions**
2. "New repository secret" 클릭
3. 추가:
   ```
   Name: VERCEL_TOKEN
   Value: [2단계에서 복사한 토큰]
   ```

### 4️⃣ 테스트 (1분)

```bash
git add .
git commit -m "feat: CI/CD 설정"
git push origin main
```

→ GitHub Actions 탭에서 배포 확인!

## ✅ 완료!

이제 `main` 브랜치에 push하면 자동으로 Vercel에 배포됩니다!

## 📖 상세 가이드

더 자세한 내용은 [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md) 참고
