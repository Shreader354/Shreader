import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl, os

client = commands.Bot( command_prefix = "." )

@client.event

async def on_ready():
	print( 'BOT connected' )
#Commands1
@client.command( pass_context = True )

async def hello (ctx):
	await ctx.send ('Ты ебанутый хули ты здароваешся ?')
#commands2
@client.command( pass_context = True )

async def GG (ctx):
	await ctx.send ('Нихуя ты пидорас')	


#clear message
@client.command( pass_context = True )

async def clear( ctx, amount = 100 ):
	await ctx.channel.purge( limit = amount )
#Авто выдача роли


#Youtube
@client.command()
async def play(ctx, url : str):
	song_there = os.path.isfile('song.mp3')

	try:
		if song_there:
			os.remove('song.mp3')
			print('[log] Старый файл удален')
	except PermissionError:
	 	print('[log] Не удалось удалить файл')

	await ctx.send('Пожалуйста ожидайте')

	voice = get(client.voice_clients, guild = ctx.guild)		

	ydl_opts = {
		'format' : 'bestaudio/best',
        'postprocessors' : [{
        	'key' : 'FFmpegExtractAudio',
        	'preferredcodec' : 'mp3',
        	'preferredquality' : '192'
        }],     
    }	

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		print('[log] загружаю музыку')
		ydl.download([url])
	for file in os.listdir('./'):
		if file.endswith('.mp3'):
			name = file
			print('[log] Переименовываю файл: {file}')
			os.rename(file, 'song.mp3')

	voice.play(discord.FFmpegPCMAudio('song.mp3'), after= lambda e: print(f'[log]{name}, музыка закончиила свое проигрывание'))
	voice.source = discord.PCMVolumeTransformer(voice.source)
	vioce.source.volume = 0.07

	song_name = name.rsplit('-', 2)
	await ctx.send(f'сейчас проигрывается музыка: {song_name[0]}')
#Голосовой чат
@client.command()
async def join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guil = ctx.guild)

	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
		await ctx.send(F'Бот присоеденился к каналу {channel}')

@client.command()
async def leave(ctx):
	
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guil = ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnect()
	else:
		voice = await connect.channel()
		await ctx.send(F'Бот отключился от канала {channel}')		


#connect
client.run('Njk4NTM0MTUwNDMyMzU4NDEx.XpHYnQ.Jr1ZnVEq8WlnsPVexnS_4yilY6g')


