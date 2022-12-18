import discord
from discord.ext import commands
from util import add_commands
from datetime import datetime
import os
import random
from keep_alive import keep_alive

TOKEN = os.getenv("token")
bot = commands.Bot(command_prefix=".kento ")
bot2 = commands.Bot(command_prefix=".ronak ")

@bot2.command()
async def congrats(ctx, num_times=None): 
    message = "Good job Ronak!"
    if (num_times == None):
        num_times = 1

    if int(num_times) > 1000:
        await ctx.send("We don't want to ping him too many times")
        return

    finalMessage = ""
    for i in range(int(num_times)):
        finalMessage += message + "\n"
    await ctx.send(finalMessage[:2000])

@bot.command()
async def describe(ctx):
    DESCRIPTION = "Kento Nishi: the harvard-accepted-top-300-sts-usaco-gold-ml-researcher-livetl-creator-web-developer-high-schooler gigachad"
    await ctx.send(DESCRIPTION)


@bot.command()
async def achievements(ctx):
    achievements = ['Full Ride @ Harvard', 'Top 300 STS Scholar', 'ML Researcher',
                    'LiveTL Creator', 'USACO Gold', 'High Schooler', 'Gigachad']
    response = ""
    for i in range(len(achievements)):
        response += f"{i + 1}." + achievements[i] + "." + "\n"
    await ctx.send(response)

@bot.command()
async def admissions(ctx): 
    results = ['Harvard (REA): Accepted', 'MIT: Basically Accepted', 'UC Berkeley EECS: Accepted (SEED Scholar Invitation)', 'UCLA CS: Accepted (Regents Invitation)', 'UCSD CS: Accepted (Regents Scholar)', 'UCSB CS: Accepted (Regents Scholar)', 'UCI CS: Accepted (Honors College)', 'Georgia Tech CS: Accepted', 'University of Maryland CS: Accepted (College Park Scholar)', 'CMU SCS: Waitlisted', 'UIUC CS: Waitlisted', 'Stanford: Rejected', 'Cornell CS: Rejected']
    resultString = ""
    for result in results: 
        resultString += result + "\n"
    await ctx.send(resultString)

@bot.command()
async def congratulate(ctx, num_times=None):
    message = "Happy 18-th birthday Kento! Now there's no need to hide that you watch NSFW stuff."
    if (num_times == None):
        num_times = 1

    if int(num_times) > 1000:
        await ctx.send("We don't want to ping him too many times")
        return

    finalMessage = ""
    for i in range(int(num_times)):
        finalMessage += message + "\n"
    await ctx.send(finalMessage[:2000])


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
             website, achievements, github, pic, admissions])

add_commands(bot2, [congrats])

keep_alive()
bot.run(TOKEN)
bot2.run(TOKEN)
