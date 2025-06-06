FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

ENV UV_VENV_MANAGED=off \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=gestion_pedidos.settings.development

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync

COPY . .

EXPOSE 8000

CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]
