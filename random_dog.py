import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import aiohttp

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_API_KEY")

client = commands.Bot(command_prefix='!')

@client.command(name='randomdog')
async def random_dog(context):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://random.dog/woof.json") as r:
            
            data = await r.json()
            embed = discord.Embed(
                title="Doggo",
                color = context.author.color
            )
            embed.set_image(url=data['url'])
            await context.send(embed=embed)


client.run(DISCORD_TOKEN)