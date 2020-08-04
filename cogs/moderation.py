import discord
from discord.ext import commands
from asyncio import sleep


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.client = bot


    @commands.command(name = "clear")
    async def clear(self, ctx, number=None):
        try:
            if number is None:
                noargem = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Не были введены аргументы")
                await ctx.send(embed=noargem)
            else:
                if ctx.author.guild_permissions.manage_messages is True:
                    if number == 0:
                        ember = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Введите число от 1 до 99")
                        await ctx.send(embed=ember)
                    if number > 99:
                        ember = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Введите число от 1 до 99")
                        await ctx.send(embed=ember)
                    else:
                        number = int(number)
                        await ctx.channel.purge(limit=number+1)
                        await sleep(2.5)
                        embed = discord.Embed(title="!clear", color=2899536, description=f"Было удалено {number} сообщений")
                        await ctx.send(embed=embed, delete_after=1.5)
                else:
                    permer = discord.Embed(title="Ошибка", color=discord.Color.red(), description="У вас недостаточно прав")
                    await ctx.send(embed=permer)
        except TypeError:
            embe = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Аргумент должен быть числом")
            await ctx.send(embed=embe)


    @commands.command(name="ban")
    async def ban(self, ctx, member : discord.User = None, *, args=None):
        if ctx.author.guild_permissions.ban_members is True:
            if member is None:
                noargem = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Не были введены аргументы")
                await ctx.send(embed=noargem)
            else:
                if member == ctx.message.author:
                    nou = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Вы не можете забанить себя")
                    await ctx.send(embed=nou)
                else:
                    banmsg = discord.Embed(title="Бан", color=discord.Color.dark_blue(),
                                           description=f"Пользователь {member} был забанен!\nПричина: **{args}**")
                    await ctx.send(embed=banmsg)
                    dmmsg = discord.Embed(title=f"{ctx.guild.name}", color=discord.Color.red(), description=f"Вы были забанены на сервере **{ctx.guild.name}**!\nПричина: **{args}**")
                    await member.send(embed=dmmsg)
                    await ctx.guild.ban(user=member, reason=args)
        else:
            embeder = discord.Embed(title="Ошибка", color=discord.Color.red(),
                                    description="У вас недостаточно прав")
            await ctx.message.delete(delay=1.0)
            await ctx.send(embed=embeder, delete_after=5.0)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            nomember = discord.Embed(title="Ошибка", color=discord.Color.red(),
                                     description="Такого пользователя нету на данном сервере")
            await ctx.send(embed=nomember)


    @commands.command(name="kick")
    async def kick(self, ctx, member : discord.User = None, *, args=None):
        if ctx.author.guild_permissions.kick_members is True:
            if member is None:
                noargem = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Не были введены аргументы")
                await ctx.send(embed=noargem)
            else:
                if member == ctx.message.author:
                    nou = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Вы не можете кикнуть себя")
                    await ctx.send(embed=nou)
                else:
                    banmsg = discord.Embed(title="Бан", color=discord.Color.dark_blue(),
                                           description=f"Пользователь {member} был кикнут!\nПричина: **{args}**")
                    await ctx.send(embed=banmsg)
                    dmmsg = discord.Embed(title=f"{ctx.guild.name}", color=discord.Color.red(), description=f"Вас кикнули с сервера **{ctx.guild.name}**!\nПричина: **{args}**")
                    await member.send(embed=dmmsg)
                    await ctx.guild.kick(user=member, reason=args)
        else:
            embeder = discord.Embed(title="Ошибка", color=discord.Color.red(),
                                    description="У вас недостаточно прав")
            await ctx.message.delete(delay=1.0)
            await ctx.send(embed=embeder, delete_after=5.0)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            nomember = discord.Embed(title="Ошибка", color=discord.Color.red(),
                                     description="Такого пользователя нету на данном сервере")
            await ctx.send(embed=nomember)


    #@commands.command(name="mute")
    #async def mute(self, ctx, member : discord.User = None, *, time=None, args=None):





def setup(bot):
    bot.add_cog(Moderation(bot))
