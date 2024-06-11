import discord
import os
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ooho(ctx):
    img_name = random.choice(os.listdir("ooho"))
    with open(f'ooho/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def Steklo(ctx):
    img_name = random.choice(os.listdir("стекло"))
    with open(f'стекло/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def Plastic(ctx):
    img_name = random.choice(os.listdir("пластик"))
    with open(f'пластик/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def Batareyka(ctx):
    img_name = random.choice(os.listdir("батареки"))
    with open(f'батареки/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

bot.run("")