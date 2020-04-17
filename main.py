import discord
import random
from discord.ext import commands
from PIL import Image, ImageEnhance, ImageOps, ImageDraw, ImageFilter
from io import BytesIO
import requests


client = commands.Bot(command_prefix = '!')
TOKEN = 'NjM3NzUwNzU3MzE5MjQ1ODM1.XbSttA.FwgfcNENFVZZognRtynzzPeoArI'



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="support - @EdS#0272", url="https://www.twitch.tv/eds52", type=discord.ActivityType.watching))
    print("Bot is ready.")






@client.command()
async def ping(ctx):
    embed = discord.Embed(colour=0x5180EC)
    embed.add_field(name="Заддержка", value=f"**Твоя заддержка** - {client.latency * 1000}ms")
    await ctx.send(embed=embed)

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question=None):
    responses = ['Да :white_check_mark:',
                 'Нет :x:',
                 'Возможно',
                 'Никак нет :name_badge:']
    embed = discord.Embed(title = 'Волшебный шар', colour=discord.Colour.purple())
    embed.add_field(name="**Вопрос:**", value=question)
    embed.add_field(name="**Ответ:**", value=f"{random.choice(responses)}")
    embedError = discord.Embed(title="Ошибка", description="Не были введены аргемуенты")
    if question == None:
        await ctx.send(embed=embedError)
        return
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def case(ctx, arg1, arg2):
    if arg1 == 'open' and arg2 == 'dlore':

        responses = ['awp басков',
                     'егор криг',
                     'калаш малахов',
                     'дигл пугачёва']
        await ctx.send(f'Вам выпало - {random.choice(responses)}')

@client.command(pass_context=True)
async def avatar(ctx):
    response = requests.get(ctx.author.avatar_url)
    im = Image.open(BytesIO(response.content))
    with BytesIO() as image_binary:
        im.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename="image.png"))



@client.command(pass_context=True)
async def me(ctx):
    await ctx.send(more)


@client.command(pass_context=True)
async def emhelp(ctx):
    embed = discord.Embed(
        title = "FMS",
        description = "Привет! Ты зашёл на сервер FMS. Что значит FMS? FMS - **FragMovie Server**. Здесь собраны различные мувимейкеры. Также сам основатель (EdS) является начанающим мувимейкером. Ознакомится с YouTube каналом можно в **Профиле** >> **Интеграции**.",
        colour=discord.Colour.blurple()
    )
    embed.add_field(name='Каналы',value='<#687978300508864540> - начальная ифнормация про сервер\n<#687977797905416250> - правила, чё не понятного\n<#688083106624045058> - роли на сервере\n<#688426291778682959> - новости\n<#688427439092662273> - общий чат\n<#688425575890550856> - чат без парвил (пс..замуть его чтоб не мешал)',inline=True)
    await ctx.send(embed=embed)


client.run(TOKEN)