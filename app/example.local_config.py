DB_URL = "postgresql://user:password@host:port/database"
JWT_SECRET_KEY = "..."

# : "id" -> { "hashed_password": ..., ... }
API_USERS = {
    "user1@test.com": {
        "id": "user1@test.com",
        "hashed_password": "...",
        "disabled": False,
        "can_access_docs": True,
        "can_access_api_read": True,
    },
}

DOMAIN = "mindfeeder.app"

CORS_ORIGINS = [
    "https://mindfeeder.app",
    "http://localhost:5000",
]
