FROM python:3.11-slim-buster


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH app

WORKDIR /app
RUN pip install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root
COPY main.py api/ /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]