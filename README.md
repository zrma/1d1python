# 1d1python

[![CI](https://github.com/zrma/1d1python/workflows/CI/badge.svg)](https://github.com/zrma/1d1python/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=1d1python&metric=alert_status)](https://sonarcloud.io/dashboard?id=1d1python)
[![Coverage Status](https://coveralls.io/repos/github/zrma/1d1python/badge.svg?branch=master)](https://coveralls.io/github/zrma/1d1python?branch=master)
[![Codecov Status](https://codecov.io/gh/zrma/1d1python/branch/master/graphs/badge.svg)](https://codecov.io/gh/zrma/1d1python)

[![DeepSource](https://deepsource.io/gh/zrma/1d1python.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/zrma/1d1python/?ref=repository-badge)
[![DeepSource](https://deepsource.io/gh/zrma/1d1python.svg/?label=resolved+issues&show_trend=true)](https://deepsource.io/gh/zrma/1d1python/?ref=repository-badge)

1 day 1 coding with python

## Requirements

- uv
- direnv

## 설치 및 설정

```shell
# uv 설치
$ curl -LsSf https://astral.sh/uv/0.6.13/install.sh | sh

# direnv 설치
$ curl -sfL https://direnv.net/install.sh | bash
$ direnv allow
$ echo "direnv 설정이 완료되었습니다. 이 디렉토리에 진입하면 환경이 자동으로 활성화됩니다."

# 개발 환경 설정
$ uv sync

# pre-commit 설치
$ pre-commit install
```

## Test on Docker

```shell
./test.sh
```
