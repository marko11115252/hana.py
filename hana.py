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

#bot responds to nani

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
				 'MYA-NEEEE :cry:',
				 'https://tenor.com/view/wataten-gif-13822468',
				 'https://tenor.com/view/wataten-watashi-ni-tenshi-ga-maiorita-idea-hinata-ihave-an-idea-gif-16051349',
				 'https://tenor.com/view/wataten-watashi-ni-tenshi-ga-maiorita-pout-hinata-anime-gif-16058457',
				 'https://tenor.com/view/mya-nee-wataten-anime-gif-18441081'
				 ]
	responses = random.choice(responses)
	await ctx.send(responses)

#bot sends gif response to food

@bot.command()
async def food(ctx):
	responses = ['https://tenor.com/view/melon-pan-wataten-anime-gif-13473060',
				 'https://tenor.com/view/wataten-gif-13822468',
				 'https://tenor.com/view/wataten-watashi-ni-tenshi-ga-maiorita-hinata-hana-headpat-gif-16053520',
				 'https://tenor.com/view/wataten-watashi-ni-tenshi-ga-maiorita-nom-nom-hana-food-gif-16566741',
				 'https://tenor.com/view/anime-watashinitenshigamaiorita-wataten-watatenanangelflewdowntome-shirosakihana-gif-13356040',
				 'https://tenor.com/view/wataten-watashi-ni-tenshi-ga-maiorita-hana-stockpiling-anime-gif-16051494',
				 'https://tenor.com/view/wataten-hana-hana-shirosaki-relaxing-drinking-gif-16042275',
				 'https://tenor.com/view/ice-hana-chan-gif-19370267'
				 ]
	responses = random.choice(responses)
	await ctx.send(responses)

#bot plays mp3


@bot.command()
async def sad(ctx):
		voice_channel = ctx.author.voice
		channel = None
		if voice_channel != None:
			channel = voice_channel.channel
			vc = await channel.connect()
			sadaudio = ['sad1.mp3', 'sad2.mp3']
			sadaudio = random.choice(sadaudio)
			vc.play(discord.FFmpegPCMAudio(sadaudio))
			while vc.is_playing():
				await asyncio.sleep(.1)
			await vc.disconnect()
		else:
			await ctx.send(str(ctx.author.name) + " wa doko da?")


#bot welcomes new memeber on server

@bot.event
async def on_member_join(member):
	guild = member.guild
	if guild.system_channel != None:
		to_send = (f'Kon\'nichiwa {member.name}, issho ni asobou!')
		await guild.system_channel.send(to_send)


#token

bot.run('your token here')
