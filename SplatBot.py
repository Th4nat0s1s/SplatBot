import discord
from discord.ext import commands

description = '''A fresh Bot for all of your Splatoon needs!'''

bot = commands.Bot(command_prefix='//', description=description)

@bot.event
async def on_ready():
   print("SplatBot Online!")
   print("Name: {}".format(bot.user.name))
   print("ID: {}".format(bot.user.id))
   print("-----")

@bot.command
async def ping():
    await bot.say("Pong!")

@bot.command(help="Use //reg to view the Regular Battle schedule for the next four(4) hours!")
async def reg():
    await bot.say("")

@bot.command
async def rank():
    await bot.say("")

@bot.command
async def leag():
    await bot.say("")

bot.run="redacted"
