import discord
import random
from discord.ext import commands
from PIL import Image, ImageEnhance, ImageOps, ImageDraw, ImageFilter
from io import BytesIO
import requests
import json


client = commands.Bot(command_prefix = '!')
TOKEN = 'NjM3NzUwNzU3MzE5MjQ1ODM1.XbSttA.FwgfcNENFVZZognRtynzzPeoArI'
client.remove_command("help")



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="version 0.1.3 | !help", url="https://www.twitch.tv/eds52", type=discord.ActivityType.streaming))
    print("Bot is ready.")





@client.command()
async def ping(ctx):
    embed = discord.Embed(colour=0x5180EC)
    embed.add_field(name="Заддержка", value=f"**Твоя заддержка** - {round(client.latency, 3)}ms")
    await ctx.send(embed=embed)

@client.command(name = "8ball")
async def _8ball(ctx, *, question=None):
    responses = ('Да :white_check_mark:',
                 'Нет :x:',
                 'Возможно',
                 'Никак нет :name_badge:')
    embed = discord.Embed(title = 'Волшебный шар', colour=discord.Colour.purple())
    embed.add_field(name="**Вопрос:**", value=question)
    embed.add_field(name="**Ответ:**", value=f"{random.choice(responses)}")
    embedError = discord.Embed(title="Ошибка", description="Не были введены аргемуенты")
    embedLenError = discord.Embed(title="Ошибка", description="Введите текст меньше 1024 символов")
    if question is None:
        await ctx.send(embed=embedError)
        return
    if question is not None:
        if len(question) >= 1024:
            await ctx.send(embed=embedLenError)
            return
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def server(ctx):
    regions = {
         'europe' : ":flag_eu: Европа",
        'russia' : ":flag_ru: Россия",
        'brazil' : ":flag_br: Бразилия",
        'hongkong' : ":flag_hk: Гонконг",
        'india' : ":flag_in: Индия",
        'japan' : ":flag_jp: Япония",
        'singapore' : ":flag_sg: Сингапур",
        'southafrica' : ":flag_sa: Южная Африка",
        'sydney' : ":flag_au: Сидней",
        'us-central' : ":flag_us: Центральная США",
        'us-east' : ":flag_us: Восточная США",
        'us-south' : ":flag_us: Южная США",
        'us-west' : ":flag_us: Западная США"
    }
    region = regions[str(ctx.guild.region)]
    embed = discord.Embed(title="Информация про сервер", description=f"Название сервера: **{str(ctx.guild.name)}**\nРегион сервера: **{region}**")
    embed.add_field(name="Каналы", value=f"Всего каналов: **{len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)}**\nТекстовые каналы: **{len(ctx.guild.text_channels)}**\nГолосовые каналы: **{len(ctx.guild.voice_channels)}**")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def case(ctx, arg1=None, arg2=None):
    if arg1 == 'open' and arg2 == 'dlore':

        responses = ['awp басков',
                     'егор криг',
                     'калаш малахов',
                     'дигл пугачёва']
        await ctx.send(f'Вам выпало - {random.choice(responses)}')
    if arg1 is None:
        embedNoArg = discord.Embed(title="Ошибка",description="Не были введены аргументы")
        await ctx.send(embed=embedNoArg)
    if arg1 == "open" and arg2 is None:
        embedSelectCase = discord.Embed(title="Выберите кейс из доступных")
        embedSelectCase.add_field(name="dlore",value="Не включает ничего. буквально")
        await ctx.send(embed=embedSelectCase)
    else:
        pass


@client.command(pass_context=True)
async def avatar(ctx):
    response = requests.get(ctx.author.avatar_url)
    im = Image.open(BytesIO(response.content))
    with BytesIO() as image_binary:
        im.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename="image.png"))


client.run(TOKEN)