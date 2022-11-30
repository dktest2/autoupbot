from motor.motor_asyncio import AsyncIOMotorClient

from config import DATABASE_NAME, DATABASE_URL


class Database:
    def __init__(self, uri, database_name):
        self._client = AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.misc = self.db['misc']
        self.links = self.db['links']


    async def create_links(self, link):
        await self.links.insert_one({
            "link": link,
        })

    async def get_links(self, link):
        return await self.links.find_one({"link": link})

    async def create_list(self, channel_name):
        await self.misc.insert_one({
            "channel_name": channel_name,
            "list":""
        })

    async def update_lists(self, channel_name, list_text):
        myquery = {"channel_name": channel_name}
        newvalues = {"$set": { "list": list_text}}
        return await self.misc.update_one(myquery, newvalues)

    async def get_lists(self, channel_name):
        return await self.misc.find_one({"channel_name": channel_name})

    async def delete_list(self, channel_name):
        myquery = {"channel_name": channel_name}
        return await self.misc.delete_one(myquery)

db = Database(DATABASE_URL, DATABASE_NAME)