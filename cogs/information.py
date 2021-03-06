import discord
from discord.ext import commands
from main import __version__


class Information(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command(name="help")
    async def help(self, ctx):
        mainhelp = discord.Embed(title="Информация про бота",
                                 description=f"**Текущая версия бота:**  {__version__}\n**Язык бота:**  "
                                             f"Русский\n**Часовой пояс:**  Москва (GMT+3)\n\n_**Чтобы просмотреть "
                                             f"список команд, напишите `!cmd`**_",
                                 color=0xB059E7)
        await ctx.send(embed=mainhelp)

    @commands.command(name='cmd', aliases=['cmds', 'command', 'commands'])
    async def cmd(self, ctx, arg1=None):
        if arg1 == "server":
            serverem = discord.Embed(title="Команда `!server`",
                                     description="Выдаёт информацию про данный сервер.\n\n**Пример:**\n> !server",
                                     color=0xB059E7)
            await ctx.send(embed=serverem)
        elif arg1 == "ping":
            pingem = discord.Embed(title="Команда `!ping`",
                                   description="Выдаёт задержку бота в `ms`\n\n**Пример:**\n> !ping",
                                   color=0xB059E7)
            await ctx.send(embed=pingem)
        elif arg1 == "8ball":
            ballem = discord.Embed(title="Команда `!8ball`",
                                   description="Волшебный Шар\n\n**Пример:**\n> !8ball <вопрос>",
                                   color=0xB059E7)
            await ctx.send(embed=ballem)
        elif arg1 == "avatar":
            avaem = discord.Embed(title="Команда `!avatar`",
                                  description="Присылает вашу аватарку\n\n**Пример:**\n> !avatar <пользователь*>\n* — "
                                              "необязательный аргумент",
                                  color=0xB059E7)
            await ctx.send(embed=avaem)
        elif arg1 == "clear":
            clre = discord.Embed(title="Команда `!clear`", color=0xB059E7,
                                 description="Очищает выбранное количество сообщений\n\n**Права доступа**: Управление "
                                             "сообщениями\n\n**Пример:**\n> !clear <кол-во сообщений>")
            await ctx.send(embed=clre)
        elif arg1 == "giveaway":
            giveawayem = discord.Embed(title="Команда `!giveaway`",
                                       description="Создаёт розыгрыш\n\n**Права доступа**: "
                                                   "Администратор\n\n**Пример:**\n> !giveaway <время розыгрыша в "
                                                   "секундах> <канал отправки сообщения про розыгрыш> <приз>",
                                       color=0xB059E7)
            await ctx.send(embed=giveawayem)
        elif arg1 == "ban":
            banan = discord.Embed(title="Команда `!ban`", color=0xB059E7,
                                  description="Выдаёт бан пользователю\n\n**Права доступа**: Банить "
                                              "участников\n\n**Пример:**\n> !ban <пользователь> <причина*>\n* — "
                                              "необязательный аргумент")
            await ctx.send(embed=banan)
        elif arg1 == "kick":
            kickk = discord.Embed(title="Команда `!kick`", color=0xB059E7,
                                  description="Выгоняет пользователя с сервера\n\n**Права доступа**: Выгонять "
                                              "участников\n\n**Пример:**\n> !kick <пользователь> <причина*>\n* — "
                                              "необязательный аргумент")
            await ctx.send(embed=kickk)
        elif arg1 == "invite":
            invv = discord.Embed(title="Команда `!invite`", color=0xB059E7,
                                 description="Ссылка для приглашения бота на свой сервер\n\n**Пример:**\n> !invite")
            await ctx.send(embed=invv)
        elif arg1 == "support":
            sup = discord.Embed(title="Команда `!support`", color=0xB059E7,
                                description="Ссылка на сервер поддержки бота")
            await ctx.send(embed=sup)
        elif arg1 is None:
            cmdhelp = discord.Embed(title="Чтобы просмотреть подробное описание команды, напишите `!cmd <команда>`",
                                    description="Все команды разбиты на категории.\nНиже вы сможете посмотреть все "
                                                "доступные команды.",
                                    color=0xB059E7)
            cmdhelp.add_field(name="Информация :tools:", value="`!server`, `!ping`")
            cmdhelp.add_field(name="Фан :gem:", value="`!8ball`")
            cmdhelp.add_field(name="Модерация :shield:", value="`!clear`, `!ban`, `!kick`")
            cmdhelp.add_field(name="Утилиты :gear:", value="`!avatar`, `!giveaway`")
            cmdhelp.add_field(name="Прочее :link:", value="`!invite`, `!support`")
            await ctx.send(embed=cmdhelp)
        else:
            nocmd = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Такой команды не существует")
            await ctx.message.delete(delay=0.5)
            await ctx.send(embed=nocmd, delete_after=5.0)

    @commands.command(name='ping')
    async def ping(self, ctx):
        embed = discord.Embed(colour=0x5180EC)
        embed.add_field(name="Заддержка", value=f"**Текущая заддержка бота** - {round(self.client.latency, 3)}ms")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, name="server")
    async def server(self, ctx):
        regions = {
            'europe': ":flag_eu: Европа",
            'russia': ":flag_ru: Россия",
            'brazil': ":flag_br: Бразилия",
            'hongkong': ":flag_hk: Гонконг",
            'india': ":flag_in: Индия",
            'japan': ":flag_jp: Япония",
            'singapore': ":flag_sg: Сингапур",
            'southafrica': ":flag_sa: Южная Африка",
            'sydney': ":flag_au: Сидней",
            'us-central': ":flag_us: Центральная США",
            'us-east': ":flag_us: Восточная США",
            'us-south': ":flag_us: Южная США",
            'us-west': ":flag_us: Западная США"
        }
        region = regions[str(ctx.guild.region)]
        embed = discord.Embed(title="Информация про сервер",
                              description=f"Название сервера: **{str(ctx.guild.name)}**\nРегион сервера: **{region}**")
        embed.add_field(name="Каналы",
                        value=f"Всего каналов: **{len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)}**\n"
                              f"Текстовые каналы: **{len(ctx.guild.text_channels)}**\nГолосовые кана"
                              f"лы: **{len(ctx.guild.voice_channels)}**")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


# Loading a cog
def setup(bot):
    bot.add_cog(Information(bot))
