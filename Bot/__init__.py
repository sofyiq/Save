from pyrogram import Client
import pyromod
# @BENN_DEV & @BENfiles

api_id = 00000
api_hash = "hash"
bot_token = "token"


app = Client(
    name = "MediaDownloader", 
    api_id = api_id, 
    api_hash = api_hash, 
    bot_token = bot_token,
    in_memory=True, 
    plugins=dict(root="Bot/handlers")
)