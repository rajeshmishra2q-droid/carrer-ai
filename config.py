import os

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

class Config:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    DEBUG = True
    PORT = 5000
    HOST = "0.0.0.0"
    CORS_ORIGINS = "*"