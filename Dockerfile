FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN poetry install --no-root

COPY . /app/

RUN mkdir -p /app/staticfiles && chmod -R 755 /app/staticfiles

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]