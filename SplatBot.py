import discord
from discord.ext import commands
import aiohttp
import asyncio
import async_timeout
import requests


description = '''A fresh Bot for all of your Splatoon needs!'''

bot = commands.Bot(command_prefix='//', description=description)

@bot.event
async def on_ready():
   print("SplatBot Online!")
   print("Name: {}".format(bot.user.name))
   print("ID: {}".format(bot.user.id))
   print("-----")

@bot.command(help="Use //ping to test if SplatBot is properly recieving commands!")
async def ping():
    await bot.say("Pong!")

@bot.command(help="Use //reg to view the Regular Battle mode & schedule for the next four(4) hours!")
async def reg():
    await bot.say("")
    async with aiohttp.ClientSession() as session:
        async with session.get('https://splatoon.ink/schedule.json') as splat:
            print(splat.status)
            print(await splat.text())


@bot.command(help="Use //rank to view the Ranked Battle mode & schedule for the next four(4) hours!")
async def rank():
    await bot.say("")

@bot.command(help="Use //leag to view the League Battle mode & schedule for the next four(4) hours!")
async def leag():
    await bot.say("")


bot.run="redacted"
