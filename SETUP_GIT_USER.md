# Git 사용자 정보 설정

## 현재 상태 확인

```bash
# 사용자 이름 확인
git config user.name

# 이메일 확인
git config user.email

# 모든 설정 확인
git config --list
```

## 설정 방법

### 프로젝트별 설정 (현재 프로젝트만)

```bash
cd /Users/an-yungyeong/Downloads/etf-helper

git config user.name "skyhanull"
git config user.email "anky0425@naver.com"
```

### 전역 설정 (모든 프로젝트)

```bash
git config --global user.name "skyhanull"
git config --global user.email "anky0425@naver.com"
```

## 설정 확인

```bash
# 프로젝트별 설정 확인
git config user.name
git config user.email

# 전역 설정 확인
git config --global user.name
git config --global user.email
```

## 설정 파일 위치

- 프로젝트별: `.git/config`
- 전역: `~/.gitconfig`
