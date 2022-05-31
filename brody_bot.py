#Import discord package
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load in our .env file which is a secret file containing the Discord API Token
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_API_KEY")

# Client (our bot)
client = commands.Bot(command_prefix='!')

@client.command(name='bark')
async def bark(context):
    await context.message.channel.send("WOOF BORK")

# @client.event
# async def on_ready():
#     # DO STUFF...
#     general_channel = client.get_channel(685833302246293537) #insert channel ID
#     await general_channel.send('Hello Bros!')

@client.event
async def on_message(message):
    if message.content == "give me a woof":
        general_channel = client.get_channel(685833302246293537)
        await general_channel.send('WOOF WOOF')
    await client.process_commands(message)

# Run the client on the server
client.run(DISCORD_TOKEN)