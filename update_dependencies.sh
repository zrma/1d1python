#!/bin/bash

# pyproject.toml 파일 경로
PYPROJECT="pyproject.toml"

if [ ! -f "$PYPROJECT" ]; then
  echo "오류: pyproject.toml 파일을 찾을 수 없습니다."
  exit 1
fi

# 일반 의존성 업데이트
echo "=== 일반 의존성 업데이트 ==="
# 일반 의존성 추출 (큰따옴표와 작은따옴표 처리, 버전 정보 제거)
DEPENDENCIES=$(grep -A 100 "dependencies = \[" "$PYPROJECT" |
  grep -B 100 -m 1 "\]" |
  grep -v "dependencies = \[" |
  grep -v "\]" |
  sed 's/^[ \t]*//' |
  sed 's/,$//' |
  sed 's/"//g' |
  sed "s/'//g" |
  awk -F'>=' '{print $1}')

if [ -z "$DEPENDENCIES" ]; then
  echo "의존성을 찾을 수 없습니다."
else
  for package in $DEPENDENCIES; do
    echo "패키지 업데이트 중: $package"
    uv remove "$package" && uv add "$package"
  done
fi

# 개발 의존성 업데이트
echo -e "\n=== 개발 의존성 업데이트 ==="
# 개발 의존성 추출 (dependency-groups의 dev 그룹에서 추출)
DEV_DEPENDENCIES=$(grep -A 100 "\[dependency-groups\]" "$PYPROJECT" |
  grep -A 100 "dev = \[" |
  grep -B 100 -m 1 "\]" |
  grep -v "dev = \[" |
  grep -v "\]" |
  sed 's/^[ \t]*//' |
  sed 's/,$//' |
  sed 's/"//g' |
  sed "s/'//g" |
  awk -F'>=' '{print $1}')

if [ -z "$DEV_DEPENDENCIES" ]; then
  echo "개발 의존성을 찾을 수 없습니다."
else
  for package in $DEV_DEPENDENCIES; do
    echo "개발 패키지 업데이트 중: $package"
    uv remove --group dev "$package" && uv add --group dev "$package"
  done
fi
