import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from PIL import Image, ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
import io

import requests
import shutil

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_API_KEY")

client = commands.Bot(command_prefix='!')

@client.command(name='danielvision')
async def blur(context):
    await get_image_and_apply_filter(context,ImageFilter.GaussianBlur(8))
    
@client.command(name='emboss')
async def emboss(context):
    await get_image_and_apply_filter(context, EMBOSS)

@client.command(name='enchance')
async def enchance(context):
    await get_image_and_apply_filter(context, EDGE_ENHANCE)

@client.command(name='smooth')
async def smooth(context):
    await get_image_and_apply_filter(context, SMOOTH)

@client.command(name='findedges')
async def findedges(context):
    await get_image_and_apply_filter(context, FIND_EDGES)

@client.command(name='contour')
async def contour(context):
    await get_image_and_apply_filter(context, CONTOUR)

@client.command(name='mush')
async def contour(context):
    await get_image_and_apply_filter(context, ImageFilter.MinFilter(size=5))

@client.command(name='greyscale')
async def contour(context):
    await get_image_and_apply_filter(context, ImageFilter.MinFilter(size=5))






@client.command(name='test')
async def test(context):
    messages = await context.channel.history(limit=2).flatten()
    for msg in messages:
        print(msg.content)



async def get_image_and_apply_filter(context, filter_type):
    channel = context.channel
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

            img1 = img.filter(filter_type)
            
            with io.BytesIO() as image_binary: #Convert image to binary to be able to send image will need for image manipulation
                img1.save(image_binary, 'PNG')
                image_binary.seek(0)
                await context.send(file=discord.File(fp=image_binary,filename='img1.png'))

client.run(DISCORD_TOKEN)