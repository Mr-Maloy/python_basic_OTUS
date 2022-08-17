"""
Чтобы собрать контейнер выполните команду:
docker build . -t app

Чтобы запустить контейнер, выполните команду:
docker run -p 8000:8000 -it app
"""
FROM python:3.10-bullseye

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry==1.1.14
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY hw_app .

EXPOSE 8000

CMD uvicorn app:app --host=0.0.0.0 --port=8000
