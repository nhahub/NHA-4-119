FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY alembic/ ./alembic/
COPY src/alembic.ini ./src/alembic.ini
COPY .env.example ./.env.example

EXPOSE 8000

CMD ["sh", "-c", "alembic -c src/alembic.ini upgrade head && uvicorn src.api.main:app --host 0.0.0.0 --port 8000"]