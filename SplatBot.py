import discord
from discord.ext import commands
import asyncio

Client = discord.Client()
bot_prefix= "!"

@client.event
async def on_ready(pass_context=True):
   print("SplatBot Online!")
   print("Name: {}".format(client.user.name))
   print("ID: {}".format(client.user.id))

@client.command
async def ping(ctx):
   await client.say("Pong!")

client.run="redacted"

@client.close
async def close():
