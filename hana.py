import discord
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = 'hana-chan ')

#bot ready message

@bot.event
async def on_ready():
	for guild in bot.guilds:
		for channel in guild.text_channels :
			if channel.name == "general" :
				await channel.send('Hana-chan wa peko peko')
				await channel.send(file=discord.File('connect.gif'))
print('Hana-chan is ready to play.')

#bot joins channel

@bot.command()
async def join(ctx):
	channel = ctx.author.voice.channel
	voiceClient = await channel.connect()

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
				 '~YAMEROOO!!!! :rage:',
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
				 'https://www.youtube.com/watch?v=A3NCtH_u8co',
				 'MYA-NEEEE :cry:']
	responses = random.choice(responses)
	await ctx.send(responses)

#bot plays mp3


@bot.command()
async def sad(ctx):
		# Gets voice channel of message author
		voice_channel = ctx.author.voice
		channel = None
		if voice_channel != None:
			channel = voice_channel.channel
			vc = await channel.connect()
			vc.play(discord.FFmpegPCMAudio('sad1.mp3'))
			while vc.is_playing():
				await asyncio.sleep(.1)
			await vc.disconnect()
		else:
			await ctx.send(str(ctx.author.name) + " wa doko da?")

#token

bot.run('your token here')
