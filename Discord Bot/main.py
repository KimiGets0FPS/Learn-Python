import os
import discord
from dotenv import load_dotenv


load_dotenv('bot_token.env')
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')
# print("{1}, {2}".format(TOKEN, GUILD))

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)
