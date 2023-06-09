import asyncio
import base64
import contextlib
import traceback
from database import db
from pyrogram import Client, filters, types
from pyrogram.errors import FloodWait

from bot import User
from config import CHANNELS, FILE_STORE_BOT_USERNAME, FILE_STORE_DB, HOTSTAR_QUALITY, MANY_BOTS, NOTIFICATION_BOT_USERNAME, \
	POST_TEMPLATE, RIP_COMMAND, SUNNXT_QUALITY, TYPE_BUTTON, VOOT_QUALITY, WEB_DL_BOT_USERNAME, ZEE5_QUALITY, type_txt, SONYLIV_QUALITY
from utils import get_cap, get_serial_info, get_short_link


@User.on_message(filters.chat(NOTIFICATION_BOT_USERNAME) & filters.regex(r'https?://[^\s]+'))
async def rip_cmd_handler(c: Client, m: types.Message):
	link = m.matches[0].group(0)
	
	if await db.get_links(link):
		return 

	fwd_msg = await c.send_message(WEB_DL_BOT_USERNAME, link)
	await fwd_msg.reply(f"{RIP_COMMAND} {link}", quote=True)

@User.on_message(filters.chat(WEB_DL_BOT_USERNAME) & (filters.regex("Checking Link...") | filters.regex("Getting Data...⌛")))
async def quality_cmd_handler(c: Client, m: types.Message):
	await asyncio.sleep(10)
	m = await c.get_messages(m.chat.id, m.id)

	link = m.reply_to_message.web_page.url if m.reply_to_message.web_page else m.reply_to_message.text
	link = link.replace(f'/{RIP_COMMAND} ', '')
	print("Starting quality button check... Sleeping for 10 seconds...")
	q = []
	if "voot" in link:
		q = VOOT_QUALITY
	elif "zee5" in link:
		q = ZEE5_QUALITY
	elif "hotstar" in link:
		q = HOTSTAR_QUALITY
	elif "sonyliv" in link:
		q = SONYLIV_QUALITY
	elif "sunnxt" in link:
		q = SUNNXT_QUALITY

	if not q:
		return

	for button in q:
		m = await c.get_messages(m.chat.id, m.id)
		for i in m.reply_markup.inline_keyboard:
			is_click = False
			for j in i:
				if j.text == button:
					with contextlib.suppress(Exception):
						await m.click(j.text)
						is_click = True
						break
			if is_click:
				break

		await asyncio.sleep(2)

@User.on_message(filters.chat(WEB_DL_BOT_USERNAME) & filters.regex(type_txt))
async def type_button_handler(_, m: types.Message):
	for i in m.reply_markup.inline_keyboard:
		for j in i:
			if j.text == TYPE_BUTTON:
				with contextlib.suppress(Exception):
					await m.click(j.text)

@User.on_message(filters.chat(WEB_DL_BOT_USERNAME) & filters.media)
async def media_handler(c: Client, m: types.Message):
	try:
		serial_link = None
		with contextlib.suppress(Exception):
			serial_link = m.reply_to_message.web_page.url if m.reply_to_message.web_page else m.reply_to_message.text 
		
		serial_link = serial_link.replace(f'{RIP_COMMAND} ', '')

		print("Serial Link: ", serial_link)

		if serial_link is None:
			return
		
		if await db.get_links(serial_link):
			return 

		caption = m.caption or ""
		caption = await get_cap(caption)

		try:
			post_message = await m.copy(chat_id=FILE_STORE_DB, disable_notification=True, caption=caption)
		except FloodWait as e:
			await asyncio.sleep(e.value)
			post_message = await m.copy(chat_id=FILE_STORE_DB, disable_notification=True, caption=caption)
		except Exception as e:
			print(e)
			return
		converted_id = post_message.id * abs(FILE_STORE_DB)
		string = f"get-{converted_id}"
		base64_string = await encode(string)
		file_store_link = f"https://telegram.me/{FILE_STORE_BOT_USERNAME}?start={base64_string}"
		serial_name, date = await get_serial_info(serial_link)
		short_link, channel, image_url = await get_short_link(file_store_link, serial_name)

		if bool(short_link and channel and image_url):
			text = POST_TEMPLATE.format(title=serial_name, date=date, short_link=short_link)
			for channel_info in CHANNELS:
				if channel.lower() == channel_info["channel_name"].lower():
					for channel_id in channel_info["channel_id"]:
						await c.send_photo(chat_id=channel_id, photo=image_url, caption=text)

			for bot in MANY_BOTS:
				await c.send_message(chat_id=bot, text="Send New Post to Subscribers")
				await asyncio.sleep(3)
				await c.send_photo(chat_id=bot, photo=image_url, caption=text)
				await c.send_message(chat_id=bot, text="Send Post to Subscribers")

			# update list
			list_text = (await db.get_lists(channel))["list"]
			list_text += f"📥 {serial_name}\n🔗 {short_link}\n\n"
			await db.update_lists(channel, list_text)
			await db.create_links(serial_link)

	except Exception as e:
		print(traceback.format_exc())

async def encode(string):
	string_bytes = string.encode("ascii")
	base64_bytes = base64.urlsafe_b64encode(string_bytes)
	return (base64_bytes.decode("ascii")).strip("=")
