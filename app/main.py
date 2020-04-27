import os, sys

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

# crap we need to do to also be able to just run `python app/main.py`...
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
)
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, "..")))

from app import config
from app.auth import (
    router as auth_router,
    User,
    get_current_active_docs_user,
)
from app.dal import db
from app.api import router as api_router


# NOTE: we'll add API docs and spec manually later [*1], auth protected
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/api/v1/auth")


@app.get("/")
def read_root():
    return PlainTextResponse(f"[{config.DOMAIN}] 🎵All you need is...")


@app.get("/api/test")
def read_test():
    return PlainTextResponse(f"[{config.DOMAIN}] 🎵All you need is...")

# [*1] re-adding API-docs next:

@app.get("/api/v1/openapi.json")
async def get_open_api_endpoint(user: User = Depends(get_current_active_docs_user)):
    return JSONResponse(get_openapi(title="FastAPI", version="1.0", routes=app.routes))


@app.get("/api/v1/docs")
async def get_documentation(user: User = Depends(get_current_active_docs_user)):
    return get_swagger_ui_html(openapi_url="/api/v1/openapi.json", title="docs")


# actual api routes
app.include_router(api_router, prefix="/api/v1")


# DEBUG mode running - run this way when needing to use a debugger (warning: auto-reload doesn't work in this mode!)
if __name__ == "__main__":
    import uvicorn  # noqa

    uvicorn.run(app, host="127.0.0.1", port=8000)
