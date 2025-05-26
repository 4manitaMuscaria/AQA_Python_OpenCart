FROM python:3.13
LABEL authors="m.zhigunov"
WORKDIR /OpenCart_autotests

ARG HOST_IP

ENV HOST_IP=$HOST_IP

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry && \
    apt-get remove -y curl && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY . .

ENTRYPOINT ["poetry", "run", "pytest"]