import logging
import os

import requests
from dotenv import load_dotenv

CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL', 'https://gist.github.com/Kousthubhbhat/e56cb4412f07ef07059c3541ae17aa86/raw')
# CONFIG_FILE_URL = 'https://gist.githubusercontent.com/kevinnadar22/4b0a7faa46e0a7398a0050d6b2934a9e/raw' \
# 	'/auto_upload_bot.env'


def write_env_file():
	if CONFIG_FILE_URL is not None:
		res = requests.get(CONFIG_FILE_URL)
		if res.status_code == 200:
			with open('.env', 'wb+') as f:
				f.write(res.content)
				f.close()
		else:
			logging.error(res.status_code)


write_env_file()
load_dotenv()

API_ID = int(os.environ.get("API_ID", "8813038"))
API_HASH = os.environ.get("API_HASH", "780fd96b159baa710dada78ff1621b54")
OWNER_ID = int(os.environ.get("OWNER_ID", "2083503061"))
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "USERBOT")
SESSION_STRING = os.environ.get("SESSION_STRING")
WEB_DL_BOT_USERNAME = os.environ.get("WEB_DL_BOT_USERNAME")
NOTIFICATION_BOT_USERNAME = os.environ.get("NOTIFICATION_BOT_USERNAME")
RIP_COMMAND = os.environ.get("RIP_COMMAND")
VOOT_QUALITY = [i.strip() for i in os.environ.get("VOOT_QUALITY").split(",")] if os.environ.get("VOOT_QUALITY") else []
HOTSTAR_QUALITY = [i.strip() for i in os.environ.get("HOTSTAR_QUALITY").split(",")] if os.environ.get("HOTSTAR_QUALITY") else []
ZEE5_QUALITY = [i.strip() for i in os.environ.get("ZEE5_QUALITY").split(",")] if os.environ.get("ZEE5_QUALITY") else []
TYPE_BUTTON = os.environ.get("TYPE_BUTTON")
MANY_BOTS = [i.strip() for i in os.environ.get("MANY_BOTS").split()] if os.environ.get("MANY_BOTS") else []
BLACKLIST_WORDS = os.environ.get("BLACKLIST_WORDS").split(",") if os.environ.get("BLACKLIST_WORDS") else [] # No space

channels = os.environ.get("CHANNELS").split(",")
# voot:-1003334 -10383484, zee5: -1001769986368
serial_shorteners = os.environ.get("SERIAL_SHORTENERS").split(",")
# Voot:Ramchari:droplink.co:1aab74171e9891abd0ba799e3fd568c9598a79e1

type_txt = "Choose Where To Upload Files, Default will be Uploaded To Telegram After 60 Sec."
quality_txt = """Select Video Format:
You Have 60 Sec."""

FILE_STORE_BOT_USERNAME = os.environ.get("FILE_STORE_BOT_USERNAME")
FILE_STORE_DB = int(os.environ.get("FILE_STORE_DB"))

POST_TEMPLATE = """🎬 Tɪᴛʟᴇ : {title}

📅 Date : {date}

➲ {short_link}

➲ {short_link}

▬▬▬▬▬▬▬▬▬▬▬▬▬▬
	🍃@serials_funda🍃
▬▬▬▬▬▬▬▬▬▬▬▬▬▬"""

SERIAL_SHORTENERS = []
for a in serial_shorteners:
	channel, serial_name, site, api, image_url = a.split()
	dic = {"serial_name": serial_name.strip().replace("<space>", " "), "site": site.strip(), "api": api.strip(),
	"channel": channel.strip().lower(), "image_url": image_url.strip()}
	SERIAL_SHORTENERS.append(dic)

CHANNELS = []

for channel in channels:
	channel_name, ids = channel.split(":")
	channel_id = [int(i.strip()) for i in ids.split()] if ids else []
	dic = {"channel_name": channel_name.strip(), "channel_id": channel_id}
	CHANNELS.append(dic)

voot_headers = {'Host': 'psapi.voot.com',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0',
		'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br', 'Referer': 'https://www.voot.com/', 'usertype': 'avod',
		'Content-Version': 'V5', 'Origin': 'https://www.voot.com', 'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'Sec-GPC': '1', 'Connection': 'keep-alive'}
zee5_headers = {'Host': 'gwapi.zee5.com',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
		'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate, br',
		'Referer': 'https://www.zee5.com/',
		'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9kdWN0X2NvZGUiOiJ6ZWU1QDk3NSIsInBsYXRmb3JtX2NvZGUiOiJXZWJAJCF0Mzg3MTIiLCJpc3N1ZWRBdCI6IjIwMjItMTAtMDRUMjA6MTQ6MzMuNzEzWiIsInR0bCI6ODY0MDAwMDAsImlhdCI6MTY2NDkxNDQ3M30.0siprWCgg7fKNhT8O8LC32zvTvUZVatXlZ1aHNvwDw8',
		'Origin': 'https://www.zee5.com', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-site', 'Sec-GPC': '1', 'Connection': 'keep-alive'}
hotstar_headers= headers= {'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0', 'Accept': ' */*', 'Accept-Language': ' eng', 'Accept-Encoding': ' gzip, deflate, br', 'Referer': ' https://www.hotstar.com/', 'x-country-code': ' IN', 'x-platform-code': ' PCTV', 'x-client-code': ' LR', 'hotstarauth': ' st=1669222094~exp=1669228094~acl=/*~hmac=47eefd6950b2da45cfddeaba7db97cf32767ab1fa60cf17a96546a021c00909b', 'x-hs-usertoken': ' eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ1bV9hY2Nlc3MiLCJleHAiOjE2Njk2MzY0NzMsImlhdCI6MTY2OTAzMTY3MywiaXNzIjoiVFMiLCJqdGkiOiIwYTkwYThlMGNmODE0YWQ1OWU5ODU4NzYzZjExYWNlZiIsInN1YiI6IntcImhJZFwiOlwiODk2MTU0NDVmZmVkNDVlM2FiYzY4NjFiZWIxMjAxZWZcIixcInBJZFwiOlwiMzQwNDBhN2E4MmRmNDJmN2EzM2MxMTBmZmM5ZjIyMmFcIixcIm5hbWVcIjpcIkd1ZXN0IFVzZXJcIixcImlwXCI6XCIxMTAuNDQuMTAuMjA0XCIsXCJjb3VudHJ5Q29kZVwiOlwiaW5cIixcImN1c3RvbWVyVHlwZVwiOlwibnVcIixcInR5cGVcIjpcImd1ZXN0XCIsXCJpc0VtYWlsVmVyaWZpZWRcIjpmYWxzZSxcImlzUGhvbmVWZXJpZmllZFwiOmZhbHNlLFwiZGV2aWNlSWRcIjpcIjg3M2ZkOGFjLWI2MzctNDAyNy04ZjMwLTc1NTZkMjhhZGMyMFwiLFwicHJvZmlsZVwiOlwiQURVTFRcIixcInZlcnNpb25cIjpcInYyXCIsXCJzdWJzY3JpcHRpb25zXCI6e1wiaW5cIjp7fX0sXCJpc3N1ZWRBdFwiOjE2NjkwMzE2NzM0MjN9IiwidmVyc2lvbiI6IjFfMCJ9.9WzjEvitAecX2qOct9gvSM-T7mimFymo3b-D7_C2_pM', 'Origin': ' https://www.hotstar.com', 'Connection': ' keep-alive', 'Sec-Fetch-Dest': ' empty', 'Sec-Fetch-Mode': ' cors', 'Sec-Fetch-Site': ' same-site', 'Sec-GPC': ' 1', 'TE': ' trailers'}

VOOT_API_URL = "https://psapi.voot.com/jio/voot/v1/voot-web/content/query/asset-details?&ids=include:{show_id}&responseType=common"
ZEE5_API_URL = "https://gwapi.zee5.com/content/tvshow/{show_id}?translation=en&country=IN"
HOTSTAR_API_URL = "https://api.hotstar.com/o/v1/show/detail?contentId={show_id}"

LIST_TEMPLATE = """2️⃣3️⃣🗡1️⃣1️⃣🗡2️⃣0️⃣2️⃣2️⃣
▬▬▬▬▬▬▬ ◆ ▬▬▬▬▬▬▬▬

ಝೀ ಕನ್ನಡ ವಾಹಿನಿಯ ಧಾರಾವಾಹಿಗಳು

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬


{}


▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
           📤 ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ 📤
           @zk_serials_bot

🚀 sʜᴀʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ ᴜs 🚀
           @serials_funda"""
