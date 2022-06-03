import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import aiohttp

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_API_KEY")

client = commands.Bot(command_prefix='!')

@client.command(name='pic')
async def random_dog(context):
    channel = context.message.channel
    #message = await channel.fetch_message(channel.last_message_id)

    async for message in channel.history(limit=2):
        if "attachments" in message.content :
             print("Content " + message.content)
             await context.message.channel.send(message.content)


    #await context.send("work")
    #await context.message.channel.send(message.content)
    

client.run(DISCORD_TOKEN)