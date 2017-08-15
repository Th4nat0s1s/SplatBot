import discord
from discord.ext import commands
import asyncio

description = '''A fresh Bot for all of your Splatoon needs!'''

bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready(pass_context=True):
   print("SplatBot Online!")
   print("Name: {}".format(bot.user.name))
   print("ID: {}".format(bot.user.id))
   print("-----")

@bot.command()
async def ping(ctx):
   await bot.say("Pong!".format(ctx))

bot.run="redacted"
