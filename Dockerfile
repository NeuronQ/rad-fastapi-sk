FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y postgresql-client-11

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# IMPORTANT: use /start.sh instead for production running
CMD ["/start-reload.sh"]
