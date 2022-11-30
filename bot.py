import logging
import logging.config
from database import db
from pyrogram import Client

from config import API_HASH, API_ID, CHANNELS, SESSION_STRING, write_env_file

# Get logging configurations
logging.getLogger().setLevel(logging.INFO)


class User(Client):
    def __init__(self):
        super().__init__(
                "user_bot",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=SESSION_STRING,
                plugins=dict(root="plugins"),
                workers=20
        )

    async def start(self):
        write_env_file()
        await super().start()

        for channel in CHANNELS:
            if not await db.get_lists(channel["channel_name"]):
                await db.create_list(channel["channel_name"])

        logging.info('User started')

    async def stop(self, *args):
        await super().stop()
        logging.info('User Stopped Bye')
