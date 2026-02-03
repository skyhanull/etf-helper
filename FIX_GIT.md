# Git 푸시 문제 해결

## 문제: "Empty repositories cannot be forked"

이 문제는 GitHub 저장소가 비어있고, 로컬 커밋이 없을 때 발생합니다.

## 해결 방법

### 방법 1: 로컬 커밋 확인 및 강제 푸시

```bash
cd /Users/an-yungyeong/Downloads/etf-helper

# 1. Git 상태 확인
git status

# 2. 커밋이 없다면 파일 추가 및 커밋
git add .
git commit -m "feat: 초기 프로젝트 설정"

# 3. 커밋 히스토리 확인
git log

# 4. 강제 푸시 (저장소가 비어있을 때)
git push -u origin main --force
```

### 방법 2: GitHub 저장소에 README 추가 후 푸시

1. GitHub 저장소 페이지에서 "Add a README" 클릭
2. README 파일 생성
3. 그 다음 로컬에서:

```bash
cd /Users/an-yungyeong/Downloads/etf-helper

# 원격 저장소의 변경사항 가져오기
git pull origin main --allow-unrelated-histories

# 충돌 해결 후
git add .
git commit -m "feat: 프로젝트 파일 추가"
git push -u origin main
```

### 방법 3: 저장소 재초기화 (가장 확실한 방법)

```bash
cd /Users/an-yungyeong/Downloads/etf-helper

# 1. 기존 Git 초기화 제거 (선택사항)
rm -rf .git

# 2. Git 재초기화
git init

# 3. 사용자 정보 설정
git config user.name "skyhanull"
git config user.email "anky0425@naver.com"

# 4. 리모트 추가
git remote add origin https://github.com/skyhanull/etf-helper.git

# 5. 파일 추가
git add .

# 6. 첫 커밋
git commit -m "feat: 초기 프로젝트 설정"

# 7. 브랜치 이름 변경
git branch -M main

# 8. 강제 푸시
git push -u origin main --force
```

## 가장 간단한 해결책

터미널에서 다음을 실행하세요:

```bash
cd /Users/an-yungyeong/Downloads/etf-helper

# 커밋 확인
git log

# 커밋이 없다면
git add .
git commit -m "feat: 초기 프로젝트 설정"

# 강제 푸시
git push -u origin main --force
```

## 주의사항

- `--force` 옵션은 원격 저장소의 내용을 덮어씁니다
- 저장소가 비어있을 때만 사용하세요
- 팀 프로젝트에서는 주의해서 사용하세요
