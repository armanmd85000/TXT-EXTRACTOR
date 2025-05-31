import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "25570420"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "6591643fa39b5b9d0eb78cb24db17f69")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "7552584508"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "7552584508 1621539522").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002322590305"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002404984636")  # Optional here you'll get all logs
