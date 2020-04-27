import os


DB_URL = "postgresql://user:password@postgresserver/db"

JWT_SECRET_KEY = ""
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 30
PASSWORD_HASHING_ALGORITHM = "HS256"

# : "id" -> { "hashed_password": ..., "disabled": True | False, ... }
# creating a user:
# 1. generate a user id:
#       openssl rand -hex 16
# 1. pick a password and hash it:
#       python
#       > from auth import get_password_hash
#       > get_password_hash("...your password...")
# 3. add user to this array
API_USERS = {}

DOMAIN = "mindfeeeder.app"

CORS_ORIGINS = [
    "https://mindfeeder.app",
]

try:
    from app.local_config import *
except ImportError:
    pass

# allow environment variable to override DOMAIN for easier dev setup
if 'DOMAIN' in os.environ:
    DOMAIN = os.environ.get('DOMAIN')
