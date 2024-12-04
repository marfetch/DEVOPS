FROM python:3-alpine

WORKDIR /usr/src/app

RUN pip install --no-cache-dir psycopg2-binary Flask

COPY . .

CMD ["python", "app.py"]
