import os

if os.environ.get("APP_ENV") != "prod":
    from dotenv import load_dotenv
    load_dotenv()
