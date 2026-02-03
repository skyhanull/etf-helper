# Git 초기화 및 GitHub 푸시 가이드

## 문제 해결

Vercel에서 Root Directory를 `frontend`로 변경할 수 없는 이유는 **GitHub에 파일이 푸시되지 않았기 때문**입니다.

## 해결 방법

### 1단계: Git 저장소 초기화

```bash
cd /Users/an-yungyeong/Downloads/etf-helper
git init
```

### 2단계: 모든 파일 추가

```bash
git add .
```

### 3단계: 첫 커밋

```bash
git commit -m "feat: 초기 프로젝트 설정"
```

### 4단계: GitHub 저장소 생성

1. [GitHub](https://github.com)에 로그인
2. "New repository" 클릭
3. 저장소 이름: `etf-helper` (또는 원하는 이름)
4. **"Initialize this repository with a README" 체크 해제** (이미 README가 있으므로)
5. "Create repository" 클릭

### 5단계: GitHub에 푸시

GitHub에서 생성한 저장소의 URL을 복사한 후:

```bash
git remote add origin https://github.com/YOUR_USERNAME/etf-helper.git
git branch -M main
git push -u origin main
```

**또는 SSH를 사용하는 경우:**

```bash
git remote add origin git@github.com:YOUR_USERNAME/etf-helper.git
git branch -M main
git push -u origin main
```

### 6단계: Vercel에서 다시 시도

GitHub에 푸시한 후:

1. Vercel Dashboard로 돌아가기
2. 프로젝트 삭제 후 다시 생성 (또는 기존 프로젝트에서 "Settings" → "Git" → "Reconnect")
3. 이제 Root Directory를 `frontend`로 변경할 수 있습니다!

## 빠른 명령어 (한 번에 실행)

```bash
cd /Users/an-yungyeong/Downloads/etf-helper

# Git 초기화
git init

# 파일 추가
git add .

# 커밋
git commit -m "feat: 초기 프로젝트 설정"

# GitHub 저장소 URL 추가 (YOUR_USERNAME과 저장소 이름 변경 필요)
git remote add origin https://github.com/YOUR_USERNAME/etf-helper.git

# 브랜치 이름 변경
git branch -M main

# 푸시
git push -u origin main
```

## 확인 방법

GitHub 저장소 페이지에서 `frontend` 폴더가 보이는지 확인하세요.

## 참고

- GitHub 저장소가 이미 있다면, `git remote add origin` 대신 `git remote set-url origin`을 사용하세요.
- 저장소 이름이 다르다면 URL을 맞게 수정하세요.
