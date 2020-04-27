#!/usr/bin/env sh
export BIND="unix:/tmp/yourthing-api-gunicorn.sock"
/home/andrei/.pyenv/versions/yourthing-poc-api/bin/gunicorn \
  -k uvicorn.workers.UvicornWorker \
  -c /opt/app/gunicorn_conf.py \
  app.main:app
