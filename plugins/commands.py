import os
import sys

from pyrogram import Client, filters, types
from database import db
from bot import User
from config import CHANNELS, LIST_TEMPLATE, OWNER_ID


@User.on_message(filters.command("start", prefixes="!"))
async def start_cmd_handler(c: Client, m: types.Message):
    await m.edit("Hey, Wassup!")


@User.on_message(filters.command("restart", prefixes="!") & filters.user(OWNER_ID))
async def restart_cmd_handler(c: Client, m: types.Message):
    await m.edit("restarting...")
    restart()

@User.on_message(filters.command("view_list", prefixes="!") & filters.user(OWNER_ID))
async def view_list_cmd_handler(c: Client, m: types.Message):
    channel_name = m.command[1].lower() if len(m.command) > 1 else None

    if not channel_name:
        editable = await m.edit("!view_list channel_name")
        return 

    list_text = await db.get_lists(channel_name)

    if not list_text:
        editable = await m.edit("Channel name not found")
        return 

    if list_text["list"]:
        await m.reply(LIST_TEMPLATE.format(list_text["list"]))


@User.on_message(filters.command("send_list", prefixes="!") & filters.user(OWNER_ID))
async def send_list_cmd_handler(c: Client, m: types.Message):
    editable = await m.edit("Broadcasting lists")
    channel_name = m.command[1].lower() if len(m.command) > 1 else None
    list_text = m.reply_to_message.text.html if  m.reply_to_message else None
    if not channel_name or not list_text:
        editable = await editable.edit("Reply to the list with channel name")
        return 

    for channel in CHANNELS:
        if channel["channel_name"] == channel_name:
            for channel_id in channel["channel_id"]:
                await c.send_message(chat_id=channel_id, text=list_text)
            await editable.edit("Done")
            await db.update_lists(channel_name, "")
            break

def restart():
    os.execv(sys.executable, ['python'] + sys.argv)

