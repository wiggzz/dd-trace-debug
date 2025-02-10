# Reproducing an issue in ddtrace

## Prerequisites

Install `uv`.

## Install

```bash
uv sync
```

## Run this app locally

```bash
uv run ddtrace-run fastapi run main.py
```

Hit `http://localhost:8080/error`.

Note that the traces from this endpoint are not shown in datadog.
