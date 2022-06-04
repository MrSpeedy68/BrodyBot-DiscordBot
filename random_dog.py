import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import urllib.request
from PIL import Image
import io

import requests
import shutil

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_API_KEY")

client = commands.Bot(command_prefix='!')

@client.command(name='pic')
async def random_dog(context):
    channel = context.message.channel
    #message = await channel.fetch_message(channel.last_message_id)

    async for message in channel.history(limit=2):
        if "attachments" in message.content :
            URL = message.content #Get Image URL if it is present
            print(URL)

            r = requests.get(URL,stream=True) #Call a requeest to that URL to fetch the image
            if r.status_code == 200:
                with open("img.png", 'wb') as f: #Open the image and set as "img.png" and decode file and set as object
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
            del r

            img = Image.open("img.png") #Use Pillow to open file
            #img.show()
            
            with io.BytesIO() as image_binary: #Convert image to binary to be able to send image will need for image manipulation
                img.save(image_binary, 'PNG')
                image_binary.seek(0)
                await context.send(file=discord.File(fp=image_binary,filename='img.png'))
    

client.run(DISCORD_TOKEN)