#Import discord package
import discord
import os
from dotenv import load_dotenv

# Load in our .env file which is a secret file containing the Discord API Token
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_API_KEY")

# Client (our bot)
client = discord.Client()

@client.event
async def on_ready():
    # DO STUFF...
    general_channel = client.get_channel(685831799880155153) #insert channel ID

    await general_channel.send('Hello Bros!')

# Run the client on the server
client.run(DISCORD_TOKEN)