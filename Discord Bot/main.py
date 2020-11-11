import discord
from discord.ext import commands
# from discord.ext.commands import Bot

from dotenv import load_dotenv
import asyncio

import random as r
import os


load_dotenv('bot_token.env')
TOKEN = os.getenv('BOT_TOKEN')
GUILD = os.getenv('BOT_GUILD')
# print(f"{TOKEN}, {GUILD}")

Client = discord.Client()
client = commands.Bot(command_prefix="%")


def get_secondary_command(message):
    return message


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


@client.command(name='search', help="%search (place)\n\nPlace list: Electrical, Admin, Lower Engine, Upper "
                                    "Engine, O2, Cafeteria, Navigation, Reactor, Medbay, Weapons, Shields, Storage"
                                    "\n\nBased on the map Skield in the real game.")
async def search(message, place_to_search):
    place_to_search = place_to_search.title()
    things_you_can_get = ['knife', 'coins', 'massive Tongue', 'hair dyer', "crewmate's keycard", 'nothing', 'missile',
                          'nothing', 'nothing', 'ejected', 'gun']
    choices_4_kill = ['Electrical', 'Admin', 'Lower Engine', 'Upper Engine', 'O2', 'Cafeteria', 'Navigation',
                      'Reactor', 'Medbay', 'Weapons', 'Shields', 'Storage']
    if place_to_search not in choices_4_kill or place_to_search == None:
        await message.channel.send(f'What are you even thinking {message.author.mention}, that is not a aviable place to'
                                   f' search/do your bussiness.')
    else:
        wat_u_get = r.choice(things_you_can_get)
        wat_u_get_2 = r.choice(things_you_can_get)
        if wat_u_get == 'ejected' or wat_u_get_2 == 'ejected':
            await message.channel.send(f"{message.author.mention} got caught doing some 'sus' stuff, and got ejected!")
        elif wat_u_get == 'nothing':
            await message.channel.send(f'{message.author.mention} got {wat_u_get_2}')
        elif wat_u_get_2 == 'nothing':
            await message.channel.send(f'{message.author.mention} got {wat_u_get}')
        elif wat_u_get and wat_u_get_2 == 'nothing':
            await message.channel.send(f'{message.author.mention} got nothing!')
        else:
            await message.channel.send(f'{message.author.mention} got a {wat_u_get} and a {wat_u_get_2}!')
    """await message.channel.send(f'Where do you want to search {message.author.mention}? \n the list of places you can'
                               f' search is {choices_4_kill}')
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
    @client.command()
    async def choose_place(place_choice):
        random_thing = r.choice(things_you_can_get)
        if random_thing == 'coin':
            await place_choice.channel.send(f'{place_choice.author.mention} searched {place_choice} and got '
                                            f'{r.randint(1, 30)}')
        else:
            await place_choice.channel.send(f'{place_choice.author.mention} searched {place_choice} and got '
                                            f'{random_thing}')"""


@client.command(name='inv', help='Use this command to see what is inside your inventory! (Still in progress for storing'
                                 ' your data')
async def inventory(message):
    await message.channel.send(f"Still in progress {message.author.mention}!")


client.run(TOKEN)
