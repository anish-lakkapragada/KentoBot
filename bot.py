import discord
from discord.ext import commands
from dotenv import dotenv_values
from util import add_commands
from datetime import datetime
import os
import random

TOKEN = dotenv_values(".env")['token']
bot = commands.Bot(command_prefix=".kento ")


@bot.command()
async def describe(ctx):
    DESCRIPTION = "Kento Nishi: the harvard-accepted-top-300-sts-usaco-gold-ml-researcher-livetl-creator-web-developer-high-schooler gigachad"
    await ctx.send(DESCRIPTION)


@bot.command()
async def achievements(ctx):
    achievements = ['Harvard Accepted', 'Top 300 STS Scholar', 'ML Researcher',
                    'LiveTL Creator', 'USACO Gold', 'High Schooler', 'Gigachad']
    response = ""
    for i in range(len(achievements)):
        response += f"{i + 1}." + achievements[i] + "." + "\n"
    await ctx.send(response)


@bot.command()
async def congratulate(ctx, num_times=None):
    message = "Happy 18-th birthday <@449366472704393216>! Now there's no need to hide that you watch NSFW stuff."
    if (num_times == None):
        num_times = 1

    if int(num_times) > 10:
        await ctx.send("We don't want to ping him too many times")
        return

    finalMessage = ""
    for i in range(int(num_times)):
        finalMessage += message + "\n"
    await ctx.send(finalMessage)


@bot.command()
async def age(ctx):
    response = "Born on February 24th, 2004 (2/22/24.)"
    delta = datetime.now() - datetime(2004, 2, 22)
    secondsAlive = delta.days * 86400 + delta.seconds
    response += f" That's {secondsAlive} seconds of wisdom!"
    await ctx.send(response)


@bot.command()
async def website(ctx):
    await ctx.send("https://kentonishi.github.io/", embed=None)


@bot.command()
async def pic(ctx):
    images_list = os.listdir("images")
    image = random.choice(images_list)
    file = discord.File(f"images/{image}")
    await ctx.send(file=file)


@bot.command()
async def github(ctx):
    await ctx.send("https://github.com/KentoNishi", embed=None)

add_commands(bot, [describe, congratulate, age,
             website, achievements, github, pic])
bot.run(TOKEN)
