# imports
import discord
from discord.ext import commands
import asyncio
import aiohttp

client = commands.Bot(command_prefix='a?') # prefix

# random.cat
@client.command()
async def cat(msg):
 if msg.author.bot: return
 async with aiohttp.ClientSession() as req:
    async with req.get('https://aws.random.cat/meow') as cat:
        cat = await cat.json()
        return await msg.channel.send(cat['file'])

# dog.ceo
@client.command()
async def dog(msg):
 if msg.author.bot: return
 async with aiohttp.ClientSession() as req:
    async with req.get('https://dog.ceo/api/breeds/image/random') as dog:
        dog = await dog.json()
        return await msg.channel.send(dog['message'])

# animals.anidiots.guide     
@client.command()
async def penguin(msg):
 if msg.author.bot: return
 async with aiohttp.ClientSession() as req:
    async with req.get('http://animals.anidiots.guide/penguin') as penguin:
        penguin = await penguin.json()
        return await msg.channel.send(penguin['link'])

@client.command()
async def panda(msg):
 if msg.author.bot: return
 async with aiohttp.ClientSession() as req:
    async with req.get('http://animals.anidiots.guide/panda') as panda:
        panda = await panda.json()
        return await msg.channel.send(panda['link'])   

@client.command()
async def tiger(msg):
 if msg.author.bot: return
 async with aiohttp.ClientSession() as req:
    async with req.get('http://animals.anidiots.guide/tiger') as tiger:
        tiger = await tiger.json()
        return await msg.channel.send(tiger['link'])

@client.command()
async def lion(msg):
 if msg.author.bot: return
 async with aiohttp.ClientSession() as req:
    async with req.get('http://animals.anidiots.guide/lion') as lion:
        lion = await lion.json()
        return await msg.channel.send(lion['link'])

@client.command()
async def redpanda(msg):
 if msg.author.bot: return
 async with aiohttp.ClientSession() as req:
    async with req.get('http://animals.anidiots.guide/red_panda') as redpanda:
        redpanda = await redpanda.json()
        return await msg.channel.send(redpanda['link'])    

# nekos.life
@client.command()
async def lizard(msg):
 if msg.author.bot: return
 async with aiohttp.ClientSession() as req:
    async with req.get('https://nekos.life/api/lizard') as lizard:
        lizard = await lizard.json()
        return await msg.channel.send(lizard['url'])       

# login
client.run('haha no')
