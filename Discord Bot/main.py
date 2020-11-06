import discord
from discord.ext import commands
# from discord.ext.commands import Bot

from dotenv import load_dotenv
import asyncio

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


@client.command()
async def error(message):
    await message.channel.send(f'There is no such command {message.author.mention}!')
"""@client.command(name='help', help='Search for a command! Remember that the prefix is %\nCommand list --> '
                                  '%kill and %search')
async def stupid_people_needing_help(message):
    await message.channel.send(f'Still in progress {message.author.mention}!')"""


@client.command(name='kill', help='Kills random amounts of people (Still in progress)')
async def kill_things(message):
    kills = r.choice([0, 0, 0, 0, 1, 1, 2])
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
        await message.channel.send(f'Where do you want to search?(type in the word)\n1. {place_1}\n2. {place_2}\n3. '
                                   f'{place_3}')

    @client.command()
    async def choose_place(place_choice):

        things_you_can_get = ['nothing', 'nothing', 'gun', 'missile', 'knife', 'ejected', 'sharp tongue',
                              'coin']
        random_thing = r.choice(things_you_can_get)
        if random_thing == 'coin':

            await place_choice.channel.send(f'{place_choice.author.mention} searched {place_choice} and got '
                                            f'{r.randint(1, 30)}')
        else:
            await place_choice.channel.send(f'{place_choice.author.mention} searched {place_choice} and got '
                                            f'{random_thing}')

# time.sleep(10)


@client.command(name='inv', help='Use this command to see what is inside your inventory! (Still in progress for '
                                 'keep in track of things)')
async def inventory(message):
    await message.channel.send(f"Still in progress {message.author.mention}!")


client.run(TOKEN)
