#!/bin/sh
DOMAIN=yourthing.local authbind --deep uvicorn app.main:app --reload --port "${1:-8000}" --host "${2:-"0.0.0.0"}"
