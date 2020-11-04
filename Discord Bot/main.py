import discord
from discord.ext import commands
# from discord.ext.commands import Bot

from dotenv import load_dotenv
import asyncio

# import time
import random as r
import os


load_dotenv('bot_token.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
# print(f"{TOKEN}, {GUILD}")


Client = discord.Client()
client = commands.Bot(command_prefix="%")


@client.event
async def on_ready():
    print("Bot is ready to operate!")


@client.command(name='help', help='Search for a command! Remember that the prefix is %\nCommand list --> '
                                  '%kill and %search')
async def stupid_people_needing_help(message):
    pass


@client.command(name='kill', help='Kills random amounts of people (Still in progress)')
async def kill_things(message):
    kills = r.choice([0, 0, 0, 0, 1, 1, 2])
    """choices_4_kill = ['Electrical', 'Admin', 'Lower Engine', 'Upper Engine', 'Oxygen Room', 'Cafeteria',
                        'Navigation', 'Reactor', 'Medbay', 'Weapons', 'Shields', 'Storage']
    place_1 = r.choice(choices_4_kill)
    place_2 = r.choice(choices_4_kill)
    place_3 = r.choice(choices_4_kill)
    await message.channel.send(f'Where do you want to kill? (type in the word)\n1. {place_1}\n2. '
                                f'{place_2}\n3. {place_3}')
    time.sleep(10)
    """
    if kills == 0:
        await message.channel.send(f'OOF! Nobody was there {message.author.mention} :(')
    else:
        await message.channel.send(f'\nWow, {message.author.mention} got {kills} kills!')
    await asyncio.sleep(30)
    # delay_message = await message.channel.send("You need to wait 30 seconds!")
    # await delay_message.delete()


@client.command(name='search', help='Use this command to search for things! First, you type in the command, then '
                                    'choose where you want to search! (Still in progress)')
async def search(message):
    choices_4_kill = ['Electrical', 'Admin', 'Lower Engine', 'Upper Engine', 'Oxygen Room', 'Cafeteria', 'Navigation',
                      'Reactor', 'Medbay', 'Weapons', 'Shields', 'Storage']
    place_1 = r.choice(choices_4_kill)
    place_2 = r.choice(choices_4_kill)
    place_3 = r.choice(choices_4_kill)
    while True:
        if place_1 == place_2:
            place_1 = r.choice(choices_4_kill)
        elif place_1 == place_3:
            place_1 = r.choice(choices_4_kill)
        elif place_2 == place_3:
            place_2 = r.choice(choices_4_kill)
        else:
            break

    @client.event(search)
    async def choose_place(place_choice):
        await message.channel.send(f'Where do you want to search?(type in the word)\n1. {place_1}\n2. {place_2}\n'
                                   f'3. {place_3}')
    # time.sleep(10)


client.run(TOKEN)
