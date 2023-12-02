from pyrogram import Client
import pyromod

app = Client(
    "MediaDownloader",
    api_id=26384753,
    api_hash="d0df15edaf47d46b36747f8af2e11b6f",
    bot_token="5249469006:AAEyC4hMWvcrZ8dTfY14dd_QTh7sqfroBO4",
    in_memory=True,
    plugins=dict(root="Bot/handlers")
)
