import os
from pyrogram import Client
import pyromod

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6646750920:AAESkHhyXID2AV58qmna0Z-RH8429o9E61c") 
APP_ID = int(os.environ.get("API_ID" , 10147860))
API_HASH = os.environ.get("API_HASH" , "e1c338d241ea26f071981e8548d40be0")

plugins = dict(
    root="plugins",
)

app = Client(
    'DDoS Management Bot',
    bot_token= BOT_TOKEN,
    api_id = APP_ID,
    api_hash= API_HASH,
    plugins=plugins
)


app.run()