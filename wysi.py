import discord
from discord.ext import tasks
import time

sentMessageToday = False

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
client = discord.Client()


@client.event
async def wysi_test(currenttime):
    global sentMessageToday

    if currenttime == "00:00" or currenttime == "12:00":
        sentMessageToday = False
    if (currenttime != "7:27" and currenttime != "19:27") or sentMessageToday:
        return
    sentMessageToday = True
    for channel in client.get_all_channels():
        if channel.type == discord.ChannelType.text:
            await channel.send("https://cdn.discordapp.com/attachments/934620054115459153/982367460273582140/images_39.jpg")
            await channel.send("727")
            await channel.send("WYSI")


@tasks.loop(seconds=10.0)
async def my_task():
    print(time.strftime("%H:%M"))
    await wysi_test(time.strftime("%H:%M"))


@client.event
async def on_ready():
    my_task.start()

client.run(token)
