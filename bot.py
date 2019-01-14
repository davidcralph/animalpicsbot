import discord
import asyncio
import aiohttp

class BotClient(discord.Client):
    async def on_ready(self):
        print('[Discord] Connected!')

    async def on_message(self, msg):
        if msg.author == self.user:
            return
            
        if msg.content.startswith('a?cat'):
            async with aiohttp.ClientSession() as req:
             async with req.get('https://aws.random.cat/meow') as cat:
              cat = await cat.json()
              return await msg.channel.send(cat["file"])

        if msg.content.startswith('a?dog'):
           async with aiohttp.ClientSession() as req:
            async with req.get('https://dog.ceo/api/breeds/image/random') as dog:
             dog = await dog.json()
             return await msg.channel.send(dog["message"])

client = BotClient()
client.run('haha no')
