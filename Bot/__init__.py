from pyrogram import Client
import pyromod

api_id = 26384753
api_hash = "d0df15edaf47d46b36747f8af2e11b6f"
bot_token = "5249469006:AAEyC4hMWvcrZ8dTfY14dd_QTh7sqfroBO4"


app = Client(
    name = "MediaDownloader", 
    api_id = api_id, 
    api_hash = api_hash, 
    bot_token = bot_token,
    in_memory=True, 
    plugins=dict(root="Bot/handlers")
)
