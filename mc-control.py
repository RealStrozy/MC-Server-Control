# mc-control.py

import os
import configparser
from discord.ext import commands
import random
import time

# Define functions


parser = configparser.ConfigParser()
bot = commands.Bot(command_prefix='!')


# Function to receive input from screen log


def fetch(ctx):
    time.sleep(12)
    logpath = "%s/logs" % mc_installpath
    print("Getting results from:" + logpath)
    loglist = os.listdir(logpath)
    loglist.sort(reverse=True)
    logpath = "%s/logs/%s" % (mc_installpath, loglist[0])
    with open(logpath, 'r') as f:
        lines = f.read().splitlines()
        output_line = lines[-1]
    scr_output = output_line[22:]
    if len(scr_output) > 1:
        return scr_output
    else:
        return "No data found"


# Global vars


install_path = os.getcwd()

# Divide INI file into global vars
parser.read('%s/config.ini' % install_path)
# Discord
dc_token = parser.get('discord', 'token')
dc_guild = parser.get('discord', 'guild')
dc_channel = parser.get('discord', 'active_channel')
# Server
server_name = parser.get('server', 'name')
mc_installpath = parser.get('server', 'mc_installpath')


# Connect to Discord bot


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# !rain


@bot.command(name='rain', help='Makes it rain or snow on the server')
async def make_rain(ctx):
    from_channel = str(ctx.channel)
    if from_channel == dc_channel:
        print("Making it clear")
        os.system("""screen -S %s -p 0 -X stuff "weather rain^M" """ % server_name)
        message = [
            "Hello Seattle!",
            "The clouds are peeing",
            "I always like walking in the rain, so no one can see me crying",
            "Rainy days should be spent at home with a cup of tea and a good book",
            "Those who hate rain hate life"
        ]
        await ctx.send(random.choice(message))
    else:
        await ctx.send("""Commands must be sent in the "server-commands" channel""")


# !clear

@bot.command(name='clear', help='Makes the weather clear')
async def make_clear(ctx):
    from_channel = str(ctx.channel)
    if from_channel == dc_channel:
        print("Making it clear")
        os.system("""screen -S %s -p 0 -X stuff "weather clear^M" """ % server_name)
        message = [
            "A cloudy day is no match for a sunny disposition!",
            "Just direct your feet to the sunny side of the street",
            "We're in the money, the skies are sunny; old man depression, you are through, you done us wrong!",
            "I don't complain when it's sunny",
            "What a bright sunny day, and I don't know what to say..."
        ]
        await ctx.send(random.choice(message))
    else:
        await ctx.send("""Commands must be sent in the "server-commands" channel""")


# !thunder


@bot.command(name='thunder', help='Makes the weather thunder')
async def make_thunder(ctx):
    from_channel = str(ctx.channel)
    if from_channel == dc_channel:
        print("Making it thunder")
        os.system("""screen -S %s -p 0 -X stuff "weather thunder^M" """ % server_name)
        message = [
            "If the tranquillity is killing you, seek for the storm to save your life!",
            "A storm will always have a chaotic chorus of accompaniment",
            "A person with storms inside does not feel the storm outside!",
            "Hard storms make great sailors",
            "When the storm seems to overpower you, hold tight, for it is only passing"
        ]
        await ctx.send(random.choice(message))
    else:
        await ctx.send("""Commands must be sent in the "server-commands" channel""")


# !sunrise


@bot.command(name='sunrise', help='Sets time to sunrise')
async def make_sunrise(ctx):
    from_channel = str(ctx.channel)
    if from_channel == dc_channel:
        print("Making it sunrise")
        os.system("""screen -S %s -p 0 -X stuff "time set sunrise^M" """ % server_name)
        message = [
            "The sun does not rise or set. The earth rotates",
            "A sunset is only half of the story",
            "Watching the sunrise every morning is a blessing",
            "The first brush of violet painted the horizon",
            "The fact that it’s a new day won’t matter if I don’t greet it with a new attitude"
        ]
        await ctx.send(random.choice(message))
    else:
        await ctx.send("""Commands must be sent in the "server-commands" channel""")


# !midnight


@bot.command(name='midnight', help='Sets time to midnight')
async def make_midnight(ctx):
    from_channel = str(ctx.channel)
    if from_channel == dc_channel:
        print("Making it midnight")
        os.system("""screen -S %s -p 0 -X stuff "time set midnight^M" """ % server_name)
        message = [
            "All great beginnings start in the dark, when the moon greets you to a new day at midnight",
            "It's almost midnight, a great time to get lost and find yourself again",
            "At midnight, in the month of June, I stand beneath the mystic moon",
            "Midnight's the only time where you can be both in the past, present, and future",
            "Welcome to the place on the other side of midnight"
        ]
        await ctx.send(random.choice(message))
    else:
        await ctx.send("""Commands must be sent in the "server-commands" channel""")


# !noon


@bot.command(name='noon', help='Sets time to noon')
async def make_noon(ctx):
    from_channel = str(ctx.channel)
    if from_channel == dc_channel:
        print("Making it clear")
        os.system("""screen -S %s -p 0 -X stuff "time set noon^M" """ % server_name)
        message = [
            "Never get out of bed before noon",
            "Nothing. And, I don't start before noon",
            "The trouble with morning is that it comes well before noon",
            "When a civilization takes up the study of itself, it is always high noon",
            "I do not believe there is life before noon"
        ]
        await ctx.send(random.choice(message))
    else:
        await ctx.send("""Commands must be sent in the "server-commands" channel""")


# !night


@bot.command(name='night', help='Sets time to night')
async def make_night(ctx):
    from_channel = str(ctx.channel)
    if from_channel == dc_channel:
        print("Making it night")
        os.system("""screen -S %s -p 0 -X stuff "time set night^M" """ % server_name)
        message = [
            "I have loved the stars too fondly to be fearful of the night",
            "How did it get so late so soon?",
            "The trouble with morning is that it comes well before noon",
            "What hath night to do with sleep?",
            "Sleep is such a luxury, which i cant afford"
        ]
        await ctx.send(random.choice(message))
    else:
        await ctx.send("""Commands must be sent in the "server-commands" channel""")


# Give objects


@bot.command(name='give', help='Gives a user an object. e.g. (!give XrayOven bucket')
async def give(ctx, *args):
    from_channel = str(ctx.channel)
    response = ""
    for arg in args:
        response = response + " " + arg
    if from_channel == dc_channel:
        print("Giving" + response)
        os.system("""screen -S %s -p 0 -X stuff "give %s %s^M" """ % (server_name, args[0], args[1]))
        message = [
            "It's not how much we give but how much love we put into giving",
            "We make a living by what we get. We make a life by what we give.",
            "Happiness doesn't result from what we get, but from what we give",
            "For it is in giving that we receive",
            "Giving does not only precede receiving; it is the reason for it. It is in giving that we receive."
        ]
        await ctx.send(random.choice(message))
    else:
        await ctx.send("""Commands must be sent in the "server-commands" channel""")


# !summon


@bot.command(name='summon', help='Summon an entity to a user. e.g. (!summon wolf XrayOven')
async def give(ctx, *args):
    from_channel = str(ctx.channel)
    if from_channel == dc_channel:
        print("Summoning" + args[0] + "to" + args[1])
        os.system(
            """screen -S %s -p 0 -X stuff "execute %s ~ ~ ~ summon %s ~ ~ ~^M" """ % (server_name, args[1], args[0])
        )
        message = [
            "A friend is someone who knows all about you and still loves you",
            "There is nothing better than a friend, unless it is a friend with chocolate",
            "I would rather walk with a friend in the dark, than alone in the light",
            "Only a true best friend can protect you from your immortal enemies",
            "I got you to look after me, and you got me to look after you, and that's why"
        ]
        await ctx.send(random.choice(message))
    else:
        await ctx.send("""Commands must be sent in the "server-commands" channel""")


# !players


@bot.command(name='players', help="List all logged in users.")
async def players(ctx):
    await ctx.send("Let me check that")
    from_channel = str(ctx.channel)
    if from_channel == dc_channel:
        os.system(
            """screen -S %s -p 0 -X stuff "list^M" """ % server_name
        )
        players_ls = fetch(ctx)
        if len(players_ls) > 2:
            if players_ls.find(",") > 0:
                if players_ls.find(",") > 1:
                    last_comma = players_ls.rindex(',')
                    players_ls = players_ls[:last_comma] + " and" + players_ls[last_comma + 1:]
                    await ctx.send(players_ls + " are online")
                else:
                    last_comma = players_ls.rindex(',')
                    players_ls = players_ls[:last_comma - 1] + " and" + players_ls[last_comma + 1:]
                    await ctx.send(players_ls + " are online")
            else:
                if players_ls != "No data found":
                    await ctx.send(players_ls + " is online")
                else:
                    await ctx.send("I can't find that. Maybe you should log in and play awhile!")
        else:
            await ctx.send("There are no players online. Sad, really...")
    else:
        await ctx.send("""Commands must be sent in the "server-commands" channel""")

bot.run(dc_token)
