# 1d1python

[![CI](https://github.com/zrma/1d1python/workflows/CI/badge.svg)](https://github.com/zrma/1d1python/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=1d1python&metric=alert_status)](https://sonarcloud.io/dashboard?id=1d1python)
[![Coverage Status](https://coveralls.io/repos/github/zrma/1d1python/badge.svg?branch=master)](https://coveralls.io/github/zrma/1d1python?branch=master)
[![Codecov Status](https://codecov.io/gh/zrma/1d1python/branch/master/graphs/badge.svg)](https://codecov.io/gh/zrma/1d1python)

[![DeepSource](https://deepsource.io/gh/zrma/1d1python.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/zrma/1d1python/?ref=repository-badge)
[![DeepSource](https://deepsource.io/gh/zrma/1d1python.svg/?label=resolved+issues&show_trend=true)](https://deepsource.io/gh/zrma/1d1python/?ref=repository-badge)

1 day 1 coding with python

## Requirement

- conda 23.11+
- python 3.12+
- make 3.81+
- rye (https://rye.astral.sh)


## Prepare

```shell
conda create -n 1d1py python=3.12
conda activate 1d1py
curl -sSf https://rye.astral.sh/get | bash
```

## pre-commit

```shell
make init
```

### Dependency

```shell
make sync-dev
```

## Test

```shell
make sync-dev
make test
```

## Test on Docker

```shell
./test.sh
```
