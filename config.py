import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
TOKEN = os.getenv("TOKEN")

# Админ ID
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# Чат ID
CHAT_ID = int(os.getenv("CHAT_ID"))