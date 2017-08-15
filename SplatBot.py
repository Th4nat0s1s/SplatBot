import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
bot_prefix= "//"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
   print("SplatBot Online!")
   print("Name: {}".format(client.user.name))
   print("ID: {}".format(client.user.id))

@client.command
async def ping(ctx):
   await client.say("Pong!")

client.run="MzQ2MzE2NjU3NjI0NDgxODI1.DHN4iQ.UMysr6idjZ9wBdfejNRu0ia,"