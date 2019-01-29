import discord
from discord.ext import commands
import asyncio
import aiohttp

client = commands.Bot(command_prefix='a?')

@client.command()
async def cat(msg):
 if msg.author.bot: return
 async with aiohttp.ClientSession() as req:
    async with req.get('https://aws.random.cat/meow') as cat:
        cat = await cat.json()
        return await msg.channel.send(cat['file'])

@client.command()
async def dog(msg):
 if msg.author.bot: return
 async with aiohttp.ClientSession() as req:
    async with req.get('https://dog.ceo/api/breeds/image/random') as dog:
        dog = await dog.json()
        return await msg.channel.send(dog['message'])
     
@client.command()
async def penguin(msg):
 if msg.author.bot: return
 async with aiohttp.ClientSession() as req:
    async with req.get('https://animals.anidiots.guide/penguin') as penguin:
        penguin = await penguin.json()
        return await msg.channel.send(penguin['link'])     
     
client.run('haha no')
