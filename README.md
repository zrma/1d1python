# 1d1python

[![CI](https://github.com/zrma/1d1python/workflows/CI/badge.svg)](https://github.com/zrma/1d1python/actions)
[![Coverage Status](https://coveralls.io/repos/github/zrma/1d1python/badge.svg?branch=main)](https://coveralls.io/github/zrma/1d1python?branch=main)
[![Codecov Status](https://codecov.io/gh/zrma/1d1python/branch/main/graphs/badge.svg)](https://codecov.io/gh/zrma/1d1python)

[![DeepSource](https://deepsource.io/gh/zrma/1d1python.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/zrma/1d1python/?ref=repository-badge)
[![DeepSource](https://deepsource.io/gh/zrma/1d1python.svg/?label=resolved+issues&show_trend=true)](https://deepsource.io/gh/zrma/1d1python/?ref=repository-badge)

1 day 1 coding with python

## Requirements

- uv
- direnv

## 설치 및 설정

```shell
# uv 설치
$ curl -LsSf https://astral.sh/uv/install.sh | sh

# direnv 설치
$ curl -sfL https://direnv.net/install.sh | bash
$ direnv allow
$ echo "direnv 설정이 완료되었습니다. 이 디렉토리에 진입하면 환경이 자동으로 활성화됩니다."

# 개발 환경 설정
$ uv sync

# pre-commit 설치
$ uv run pre-commit install
```

## Test on Docker

```shell
./test.sh
```

## 의존성 보안 검사

```sh
scripts/audit-dependencies.sh
```

`uv.lock`에서 runtime/dev 전체를 해시와 함께 export하고, 고정된 pip-audit로
검사한다. 검사를 위해 의존성을 다시 선택하거나 프로젝트를 설치하지 않는다.
신규 취약점, 조회 실패 또는 검사할 수 없는 패키지는 실패로 처리한다.
현재 등록한 취약점 예외는 없다.

공개 저장소의 `Dependency security` workflow는 lockfile·설정 변경과 매주
정기 실행에서 같은 검사를 수행한다. job은 공개 저장소에서만 실행하도록 제한한다.
