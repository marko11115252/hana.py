import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')

#bot ready message

@bot.event
async def on_ready():
	print('Hana-chan is ready to play.')

#user join message

@bot.event
async def on_member_join(member):
	print(f'{member} has joined a server.')	

#user leave message

@bot.event
async def on_member_remove(member):
	print(f'{member} has left a server.')

#bot command ping

@bot.command()
async def ping(ctx):
	await ctx.send(f'MYA-NEE! {round(bot.latency * 1000)}ms')

#bot command nani

@bot.command()
async def nani(ctx, *, question):
	responses = ['MYA-NEE!',
				 'Issoni asoboio',
				 '~YAMEROOO!!!!',
				 'EH?',
				 'Oi ningen!',
				 'Bukkorosu!',
				 'Bukkorostearu!,',
				 'OI OI OI OI OI!',
				 'Matte kudasai',
				 'Nanda kore wa?!',
				 'Kuso gaki domo',
				 'Mahou shoujo'
				 'https://www.youtube.com/watch?v=bydxMFQd3wc']
	await ctx.send(random.choice(responses)

#token

bot.run('token')
