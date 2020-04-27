# Rapid MVP/PoC API development with FastAPI

**TL/DR:** `Minimalism` ∩ `Interactive-REPL-driven-development` == ❤️❤️❤️.

---

> ⚠️ work in progress - for now intended only for author's own use ⚠️

---

# TODO

- [ ] purge things too specific to project this was extracted from
- [ ] fix Docker config and related to work standalone
- [ ] add a proper list of TODOs and start working on turning this into a proper generally usable starter kit

## Ho to set up
```shell script
# 1.
pip install -r requirements.txt

# 2.
cp example.local_config.py local_config.py

# 3.
# edit local_config.py

# 4. (locally, on your developer machine) edit hosts file adding:
#      127.0.0.1	mindfeeder.local
# HINT: this is probably simplest ways to make browsers stfu about some cross-origin issues
```

Possible ways to generate values for `local_config.py`
- `JWT_SECRET_KEY` - to generate a JWT secret key run command `openssl rand -hex 32`
- to generate a random user id (key in `API_USERS`) run command `openssl rand -hex 16`
- to generate a hash for your password (DO NOT EVER store actual password in file!): `python -c "import app.auth; print(app.auth.get_password_hash('your password here'))"`
- add/edit in `CORS_ORIGINS` to also have the url you're serving you dev frontend from (if any)


## How to run for development

Run this on local machine or on dev/testing/staging server:

```shell script
./run-dev.sh

# or with port and host (default 8000:0.0.0.0)
./run-dev.sh 80 127.0.0.1
```

## How to log in to API docs/test swagger UI

Go to `/api/v1/auth/login` in browser.

## How to run tests
```shell script
./test.sh
```

## How to run app & db shell/REPL

```shell script
# 1. if on server, ensure you ssh-d with port tunnelled,
#    eg. `-A -L 8080:localhost:8080`
# or pass one arg, port (default 8080)
./run-dev-jupyter.sh
```

---
## How to set up new deployment

**This is JUST AN EXAMPLE!**

```shell script
# set up nginx
sudo cp /opt/app/example.nginx.conf /etc/nginx/sites-available/yourthing.app
sudo ln -s /etc/nginx/sites-available/yourthing.app /etc/nginx/sites-enabled/

# configure service for gunicorn + uvicorn
sudo cp /opt/app/example.systemd.confs/yourthing-api-gunicorn.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start yourthing-api-gunicorn
```
