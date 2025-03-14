from os import environ

API_ID = int(environ.get("API_ID", "24817837"))
API_HASH = environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
BOT_TOKEN = environ.get("BOT_TOKEN", "7914809939:AAFz_dbOWQhdYdrCu0KC6KdjDFXXitkTCF87914809939:AAFz_dbOWQhdYdrCu0KC6KdjDFXXitkTCF8")
OWNER_ID = int(environ.get("OWNER_ID", "7428552084"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002376378205"))
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://altof2:123Bonjoure@cluster0.s1suq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT = int(environ.get('PORT', 8080))
AUTH_CHANNELS = environ.get("AUTH_CHANNEL", "-1002376378205")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")]
