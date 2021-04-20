import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = 'hana-chan ')

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

#bot command responses to nani

@bot.command()
async def nani(ctx):
	responses = ['MYA-NEE!',
				 'Issoni asoboio',
				 '~YAMEROOO!!!!',
				 'EH?',
				 'Oi ningen!',
				 'Bukkorosu!',
				 'Bukkorostearu!',
				 'OI OI OI OI OI!',
				 'Matte kudasai',
				 'Nanda kore wa?!',
				 'Kuso gaki domo',
				 'Mahou shoujo',
				 'https://www.youtube.com/watch?v=bydxMFQd3wc',
				 'https://www.youtube.com/watch?v=an2G10_YnXc',
				 'https://www.youtube.com/watch?v=SbSf8AAJge0',
				 'https://www.youtube.com/watch?v=9k6HVsNJu3E',
				 'https://www.youtube.com/watch?v=d3Xc18kVgco',
				 'https://www.youtube.com/watch?v=hWmasCJI1fc',
				 'https://www.youtube.com/watch?v=dkJNeLawexM',
				 'https://www.youtube.com/watch?v=A3NCtH_u8co']
	responses = random.choice(responses)
	await ctx.send(responses)

#token

bot.run('your token here')
