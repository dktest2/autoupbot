import json
import logging
import os

import requests
from dotenv import load_dotenv

CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL', 'https://gist.github.com/Bhatmanjusms/dffa17bb3e4194b7bc8f60aa2b485f6d/raw')
# CONFIG_FILE_URL = None
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

API_ID = int(os.environ.get("API_ID", "977080"))
API_HASH = os.environ.get("API_HASH", "0c20c4265501492a1513f91755acd42b")
OWNER_ID = int(os.environ.get("OWNER_ID", "399726799"))
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "USERBOT")
SESSION_STRING = os.environ.get("SESSION_STRING")
WEB_DL_BOT_USERNAME = os.environ.get("WEB_DL_BOT_USERNAME")
NOTIFICATION_BOT_USERNAME = os.environ.get("NOTIFICATION_BOT_USERNAME")
RIP_COMMAND = os.environ.get("RIP_COMMAND")
VOOT_QUALITY = [i.strip() for i in os.environ.get("VOOT_QUALITY").split(",")] if os.environ.get("VOOT_QUALITY") else []
HOTSTAR_QUALITY = [i.strip() for i in os.environ.get("HOTSTAR_QUALITY").split(",")] if os.environ.get("HOTSTAR_QUALITY") else []
ZEE5_QUALITY = [i.strip() for i in os.environ.get("ZEE5_QUALITY").split(",")] if os.environ.get("ZEE5_QUALITY") else []
SONYLIV_QUALITY = [i.strip() for i in os.environ.get("SONYLIV_QUALITY").split(",")] if os.environ.get("SONYLIV_QUALITY") else []

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

▬▬▬▬▬▬▬▬▬▬▬▬▬▬"""

SERIAL_SHORTENERS = []
for a in serial_shorteners:
	try:
		channel, serial_name, site, api, image_url = a.split()
		dic = {"serial_name": serial_name.strip().replace("<space>", " "), "site": site.strip(), "api": api.strip(),
		"channel": channel.strip().lower(), "image_url": image_url.strip()}
		SERIAL_SHORTENERS.append(dic)
	except Exception:
		print(a)

for fruit in SERIAL_SHORTENERS:
	print(json.dumps(fruit, indent=4))

	
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
		'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9kdWN0X2NvZGUiOiJ6ZWU1QDk3NSIsInBsYXRmb3JtX2NvZGUiOiJXZWJAJCF0Mzg3MTIiLCJpc3N1ZWRBdCI6IjIwMjMtMDEtMDZUMTQ6MDM6MzkuOTE5WiIsInR0bCI6ODY0MDAwMDAsImlhdCI6MTY3MzAxMzgxOX0.2Aqm3dugHB4li2f2WG0LnvoeHSqdP0YZnv21C8zxS54',
		'Origin': 'https://www.zee5.com', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-site', 'Sec-GPC': '1', 'Connection': 'keep-alive'}
hotstar_headers= headers= {'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0', 'Accept': ' */*', 'Accept-Language': ' eng', 'Accept-Encoding': ' gzip, deflate, br', 'Referer': ' https://www.hotstar.com/', 'x-country-code': ' IN', 'x-platform-code': ' PCTV', 'x-client-code': ' LR', 'hotstarauth': ' st=1669222094~exp=1669228094~acl=/*~hmac=47eefd6950b2da45cfddeaba7db97cf32767ab1fa60cf17a96546a021c00909b', 'x-hs-usertoken': ' eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ1bV9hY2Nlc3MiLCJleHAiOjE2Njk2MzY0NzMsImlhdCI6MTY2OTAzMTY3MywiaXNzIjoiVFMiLCJqdGkiOiIwYTkwYThlMGNmODE0YWQ1OWU5ODU4NzYzZjExYWNlZiIsInN1YiI6IntcImhJZFwiOlwiODk2MTU0NDVmZmVkNDVlM2FiYzY4NjFiZWIxMjAxZWZcIixcInBJZFwiOlwiMzQwNDBhN2E4MmRmNDJmN2EzM2MxMTBmZmM5ZjIyMmFcIixcIm5hbWVcIjpcIkd1ZXN0IFVzZXJcIixcImlwXCI6XCIxMTAuNDQuMTAuMjA0XCIsXCJjb3VudHJ5Q29kZVwiOlwiaW5cIixcImN1c3RvbWVyVHlwZVwiOlwibnVcIixcInR5cGVcIjpcImd1ZXN0XCIsXCJpc0VtYWlsVmVyaWZpZWRcIjpmYWxzZSxcImlzUGhvbmVWZXJpZmllZFwiOmZhbHNlLFwiZGV2aWNlSWRcIjpcIjg3M2ZkOGFjLWI2MzctNDAyNy04ZjMwLTc1NTZkMjhhZGMyMFwiLFwicHJvZmlsZVwiOlwiQURVTFRcIixcInZlcnNpb25cIjpcInYyXCIsXCJzdWJzY3JpcHRpb25zXCI6e1wiaW5cIjp7fX0sXCJpc3N1ZWRBdFwiOjE2NjkwMzE2NzM0MjN9IiwidmVyc2lvbiI6IjFfMCJ9.9WzjEvitAecX2qOct9gvSM-T7mimFymo3b-D7_C2_pM', 'Origin': ' https://www.hotstar.com', 'Connection': ' keep-alive', 'Sec-Fetch-Dest': ' empty', 'Sec-Fetch-Mode': ' cors', 'Sec-Fetch-Site': ' same-site', 'Sec-GPC': ' 1', 'TE': ' trailers'}
sonyliv_headers = {'security_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzExOTI1MTYsImV4cCI6MTY3MjQ4ODUxNiwiYXVkIjoiKi5zb255bGl2LmNvbSIsImlzcyI6IlNvbnlMSVYiLCJzdWIiOiJzb21lQHNldGluZGlhLmNvbSJ9.S2e99rs_SynMy347baAIAZTod7r3u05ErL6u7Pvwqb2GF-CN28otD8ktIk3Hpgr2cb4pwkAlrPVeLOKtyW31i7pivYfbig9NsE_X41sRC5bnauL_Eo4XM89X9K-HR5g9zUB3tqKDIMEC1ysHWz7jES-Z-ALjkg-8Ip3U6fK9l2TyP_4_ibr9dMJL7UHf-TVec1ZdFh_nTUV-diF6P06SPDOLPNYuLha88LNb1wcBtiyKWFzAbJ3XGlgqbltGWsiXLqdFlaRp8aC4W8JH0f0kSIqdxbANt-sR--In-071uZ_BvkMjFS5e9BU07Ad9jMk7T5bAdGQ1vPq-JVlTUFQXC27a2bXV5LIynnaOQ27zyZcI6o97rLL0duZ8SOInfklK7xExNZ5LJMgB1GcxGf-VO-zm00I70hrwjQghANKorRFCeCXLg0NckeyJkI_ciL9LGgb4dN9VLH4qYx-C9tgNOAFa7A_NINlzCYIuUora2yynJ9sIIMUsZqaXdtt4OgiR_od243i9CXs2EoBFdoAqda-K6RnmWEkHsx2SzbqExoemUSh1Qq2fOvu5Q_vkAI2Pv-nXQ8aXnlIeeMiZ4cet_ieFKUqS6vuFDwCqgtkX_YeL6k9f3GteEDdy6J-sNBk8eiXLkl0IMUa0hB7wbpi_h6Im2GbRpGnocWAqmB6GJnA'}
VOOT_API_URL = "https://psapi.voot.com/jio/voot/v1/voot-web/content/query/asset-details?&ids=include:{show_id}&responseType=common"
ZEE5_API_URL = "https://gwapi.zee5.com/content/tvshow/{show_id}?translation=en&country=IN"
HOTSTAR_API_URL = "https://api.hotstar.com/o/v1/show/detail?contentId={show_id}"
SONY_LIV_API_URL = "https://apiv2.sonyliv.com/AGL/2.6/A/ENG/WEB/IN/MH/CONTENT/VIDEOURL/VOD/{show_id}?kids_safe=false"

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
