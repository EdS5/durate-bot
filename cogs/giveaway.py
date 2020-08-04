import discord
from discord.ext import commands
import time
import random
from asyncio import sleep
from discord.ext.commands import errors


class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command(name="giveaway")
    async def giveaway(self, ctx, arg1=None, arg2 : discord.TextChannel=None, *, args=None):
        try:
            if ctx.author.guild_permissions.administrator is True:
                if arg1 is None or arg2 is None:
                    argEmbed = discord.Embed(title="Ошибка", description="Не были введены аргументы")
                    await ctx.send(embed=argEmbed)
                if arg1 is not None and arg2 is not None and args is None:
                    argEmbed = discord.Embed(title="Ошибка", description="Не были введены аргументы")
                    await ctx.send(embed=argEmbed)
                else:
                    CorrectlyEmbed = discord.Embed(title="Розыгрыш создан!", color=discord.Color.blue(),
                                                  description=f"**Время розыгрыша:** {arg1} секунд\n**Канал сообщения:** {arg2}\n**Приз:** {args}")
                    await ctx.message.delete(delay=1.7)
                    await ctx.send(embed=CorrectlyEmbed, delete_after=15.0)

                    channel = self.client.get_channel(arg2.id)
                    newembed = discord.Embed(title=":tada: РОЗЫГРЫШ :tada:",
                                            description=f"**Нажмите на реакцию, чтобы участвовать.**\n\n**Приз:** {args}\n**Время розыгрыша:** {arg1} секунд")
                    message = await channel.send(embed=newembed)
                    giveawayEmoji = self.client.get_emoji(731079730203459615)
                    await message.add_reaction(giveawayEmoji)


                    await sleep(int(arg1))

                    message_new = await channel.fetch_message(message.id)

                    giveawayReaction = []
                    for reaction in message_new.reactions:
                        if reaction.emoji == giveawayEmoji:
                            giveawayReaction = reaction

                    who_reacted = list(await giveawayReaction.users().flatten())
                    user_bot = discord.utils.find(lambda m: m.id == 637750757319245835, ctx.guild.members)
                    who_reacted.remove(user_bot)
                    winner = random.choice(who_reacted)
                    EmWin = discord.Embed(title="<a:dConrats:731079711815630901> ПОБЕДИТЕЛЬ <a:dConrats:731079711815630901>", color=discord.Color.blue(), description=f"{winner.mention} выиграл **{args}**!")
                    await channel.send(embed=EmWin)

            else:
                embeder = discord.Embed(title="Ошибка", color=discord.Color.red(),
                                        description="У вас недостаточно прав")
                await ctx.message.delete(delay=1.0)
                await ctx.send(embed=embeder, delete_after=5.0)

        except ValueError:
            emer = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Неправильный тип аргументов")
            await ctx.message.delete(delay=1.0)
            await ctx.send(embed=emer, delete_after=5.0)
        except TypeError:
            emere = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Победителей нет, так как никто не учавствовал")
            await ctx.send(embed=emere)

    @giveaway.error
    async def giveaway_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            emerr = discord.Embed(title="Ошибка", color=discord.Color.red(),
                                  description='Такого канала нет на данном сервере')
            await ctx.send(embed=emerr)



def setup(bot):
    bot.add_cog(Giveaway(bot))
