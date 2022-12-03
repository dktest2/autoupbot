import re
import aiohttp
import contextlib
from shortzy import Shortzy
from config import BLACKLIST_WORDS, HOTSTAR_API_URL, SERIAL_SHORTENERS, VOOT_API_URL, ZEE5_API_URL, voot_headers, zee5_headers, hotstar_headers
from datetime import datetime
import cloudscraper

async def get_serial_info(url):
	headers = await get_headers(url)
	req_url = await get_req_url(url)
	res = await get_response(req_url, headers)

	if "voot" in url:
		result = res["result"][0]
		serial_name = result["name"]
		og_date = await extract_date(result["seo"]["title"])
		return serial_name, og_date

	elif "zee5" in url:

		serial_name = res["tvshow"]["title"]
		og_date = res["extended"]["publish_datetime"].split()[0]
		return serial_name, og_date

	elif "hotstar" in url:
		try:
			res = res["body"]["results"]['trays']["items"][0]["assets"]["items"]
		except KeyError:
			res = res["body"]["results"]["trays"]["items"][1]["assets"]["items"]

		content_id = int(url.split("/")[-1])
		for info in res:
			if info["contentId"] == content_id:
				return info["showName"], unix_to_date(info["broadCastDate"])

def unix_to_date(unix):
	ts = int(unix)
	# if you encounter a "year is out of range" error the timestamp
	# may be in milliseconds, try `ts /= 1000` in that case
	return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')

async def get_response(url, headers=None):
	async with aiohttp.ClientSession(headers=headers) as session:
		async with session.get(url, raise_for_status=True) as response:
			return await response.json()


async def get_headers(url):
	headers = None
	if "voot" in url:
		headers = voot_headers
	elif "zee5" in url:
		headers = zee5_headers
	elif "hotstar" in url:
		headers = hotstar_headers
	return headers


async def extract_date(string):
	DATE_PATTERN = r"(\d{1,2})/(\d{1,2})/(\d{4})|(\d{4})-(\d{1,2})-(\d{1,2})|(\d{1,2})-(\d{1,2})-(\d{4})"
	date = re.search(DATE_PATTERN, string)
	return date.group() if date else None


async def get_req_url(url):
	show_id = url.split("/")[-1]
	if "voot.com" in url:
		return VOOT_API_URL.format(show_id=show_id)
	elif "zee5.com" in url:
		return ZEE5_API_URL.format(show_id=show_id)
	elif "hotstar.com" in url:
		show_id = filter_int(url.split("/"))
		return HOTSTAR_API_URL.format(show_id=show_id[0])

async def get_short_link(link, serial_name):
	for serial in SERIAL_SHORTENERS:
		if serial["serial_name"] == serial_name:
			api, site = serial["api"], serial["site"]
			shortzy = Shortzy(api, site)
			try:
				short_link = await shortzy.convert(link)
			except Exception:
				short_link = await get_shortlink(api, serial["site"], link)

			return short_link, serial["channel"], serial["image_url"]
	return 0,0,0

async def get_cap(caption):
	big_regex = re.compile('|'.join(map(re.escape, BLACKLIST_WORDS)))
	return big_regex.sub("", caption)

def filter_int(n_list:list)-> list:
	list_of_numbers = []
	for el in n_list:
		with contextlib.suppress(ValueError):
			list_of_numbers.append(int(el))

	return list_of_numbers

async def get_shortlink(api, site, link):
	base_url = f'https://{site}/api'
	params = {'api': api, 'url': link}
	scraper = cloudscraper.create_scraper() 
	r = scraper.get(base_url, params=params)
	return r.json()["shortenedUrl"]
