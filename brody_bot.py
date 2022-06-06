#Import discord package
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import aiohttp
from PIL import Image, ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
import io
import requests
import shutil

# Load in our .env file which is a secret file containing the Discord API Token
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_API_KEY")

# Client (our bot)
client = commands.Bot(command_prefix='!')

# BARK
@client.command(name='bark')
async def bark(context):
    await context.send("WOOF WOOF")

@client.event
async def on_message(message):
    if message.content == "give me a woof":
        general_channel = client.get_channel(685833302246293537)
        await general_channel.send('Bababooey')
    await client.process_commands(message)

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
            await context.send(embed=embed)

# BRODY PIC
@client.command(name='brodypic')
async def brodypic(context):
    await context.send("https://imgur.com/4EZsemc")

# IMAGE PROCESSING COMMANDS
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
async def mush(context):
    await get_image_and_apply_filter(context, ImageFilter.MinFilter(size=5))

@client.command(name='greyscale')
async def greyscale(context):
    await get_image_and_apply_filter(context, ImageFilter.MinFilter(size=5))


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

# Help Command
@client.command(name='!help')
async def help_commands(context):
    help_commands = "First post an image in the chat for these commands to work.\n" + "**Image Commands**\n" + "!danielvision - Blurs Photo \n" +"!emboss - Applys Filter\n" +"!enchance - attempts to improve image quality\n" +"!smooth - Smooths the image\n" +"!findedges - Applies an edge finding algo on photo\n" +"!contour - Extracts photo contour\n" +"!mush - blur the photo slightly and turn it mushy\n" +"!greyscale - turn the photo greyscale\n" +"**Server exclusive commands**\n" +"!bark - returns 'WOOF WOOF' into the chat\n" +"!randomdog - returns random media of dog (Image, GIF, Video) from random.dog/woof.json\n" +"!brodypic - returns random image of world renoun Brody Choccy lab\n" +"**Bot Responses through text**\n" +"'give me a woof' - Returns 'Babaooey'\n"
    await context.send(help_commands)


# Run the client on the server
client.run(DISCORD_TOKEN)