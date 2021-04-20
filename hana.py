import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Bot is ready.')

client.run('ODM0MDc0MjA0NjU0NjY1NzQ5.YH7mIg.lnWjS9NmOQ_h4etXpb5KHQHBr_s')