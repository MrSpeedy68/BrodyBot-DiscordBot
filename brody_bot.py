#Import discord package
import discord
import os
from dotenv import load_dotenv

# Load in our .env file which is a secret file containing the Discord API Token
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_API_KEY")

# Client (our bot)
#client = discord.Client()

# DO STUFF...

# Run the client on the server
#client.run()

print(DISCORD_TOKEN)