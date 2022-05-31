#Import discord package
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import aiohttp

# Load in our .env file which is a secret file containing the Discord API Token
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_API_KEY")

# Client (our bot)
client = commands.Bot(command_prefix='!')

# BARK
@client.command(name='bark')
async def bark(context):
    await context.message.channel.send("WOOF WOOF")

# RANDOM DOG
@client.command(name='randomdog')
async def randomdog(context):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://random.dog/woof.json") as r: #Get JSON data from link and extract the image / file url
            
            data = await r.json()
            embed = discord.Embed(
                title="Doggo",
                color = context.author.color
            )
            embed.set_image(url=data['url'])
            await context.message.channel.send(embed=embed)

# BRODY PIC
@client.command(name='brodypic')
async def brodypic(context):
    await context.message.channel.send("https://imgur.com/4EZsemc")

@client.event
async def on_message(message):
    if message.content == "give me a woof":
        general_channel = client.get_channel(685833302246293537)
        await general_channel.send('Bababooey')
    await client.process_commands(message)
    
# Run the client on the server
client.run(DISCORD_TOKEN)