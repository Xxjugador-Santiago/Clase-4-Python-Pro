import discord
import random
import os
import requests
from bot_logic import gen_pass
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix= "$", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')




@bot.command()
async def meme(ctx):
    with open("C:/Users/migue/Desktop/Escritorio/python/Bot clase 4 28-08-2024/images/mem1.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)



@bot.command()
async def meme_aleatorio(ctx):
    mem_alet = random.choice(os.listdir("C:/Users/migue/Desktop/Escritorio/python/Bot clase 4 28-08-2024/images"))
    
    with open(f"C:/Users/migue/Desktop/Escritorio/python/Bot clase 4 28-08-2024/images/{mem_alet}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)




def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)





@bot.command()
async def hello(ctx):
    await ctx.send(f"Hi!!!")

@bot.command()
async def bye(ctx):
    await ctx.send("😔")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def bothelp(ctx):
    await ctx.send(f"Comandos: $hello , $bye , $password (genera una contraseña), $cool , $joined @tu nombre (da la bienvenida)")

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run("")
