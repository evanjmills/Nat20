import asyncio
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('Nat20 is online')


@client.event
async def on_message():
    pass


client.run(TOKEN)
