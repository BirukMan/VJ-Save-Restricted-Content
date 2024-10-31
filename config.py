import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6817528487:AAEoB-XLaFQhj8JA3GHmzQn0JjC1qKx5xps")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28189050"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9c1f3da6e0af0ded16d6ecb0989d06de")

#Database 
DB_URI = os.environ.get("DB_URI", "")
