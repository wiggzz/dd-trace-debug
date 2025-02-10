# error traces are not shown in datadog

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

This creates an unprintable exception, which ddtrace fails to record as an erroneous trace. Both it and the parent trace are not shown in datadog.
