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

ARG USERNAME=ryeuser
RUN useradd ${USERNAME} --create-home
USER ${USERNAME}

WORKDIR /home/${USERNAME}/app

ENV RYE_HOME /home/${USERNAME}/.rye
ENV PATH ${RYE_HOME}/shims:${PATH}

RUN curl -sSf https://rye.astral.sh/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash && \
    rye config --set-bool behavior.global-python=true


COPY pyproject.toml ./
COPY requirements.lock ./
COPY requirements-dev.lock ./
COPY Makefile ./

RUN make sync-dev

RUN mkdir -p src
RUN mkdir -p tests

COPY src ./src
COPY tests ./tests

RUN make ruff
RUN make test
