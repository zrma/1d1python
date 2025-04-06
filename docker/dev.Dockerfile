FROM python:3.13.0b4-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    make  \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

ENV UV_PROJECT_ENVIRONMENT=/usr/local

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir uv==0.6.13 \
    && uv sync --no-dev --locked

COPY Makefile Makefile

RUN mkdir -p src
COPY src ./src
