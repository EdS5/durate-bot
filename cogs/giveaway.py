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
    async def giveaway(self, ctx, arg1=None, arg2: discord.TextChannel = None, *, args=None):
        try:
            if ctx.author.guild_permissions.administrator is True:
                if arg1 is None or arg2 is None:
                    arg_embed = discord.Embed(title="Ошибка", description="Не были введены аргументы")
                    await ctx.send(embed=arg_embed)
                if arg1 is not None and arg2 is not None and args is None:
                    arg_embed = discord.Embed(title="Ошибка", description="Не были введены аргументы")
                    await ctx.send(embed=arg_embed)
                else:
                    CorrectlyEmbed = discord.Embed(title="Розыгрыш создан!", color=discord.Color.blue(),
                                                   description=f"**Время розыгрыша:** {arg1} секунд\n**Канал "
                                                               f"сообщения:** {arg2.mention}\n**Приз:** {args}")
                    await ctx.message.delete(delay=1.7)
                    await ctx.send(embed=CorrectlyEmbed, delete_after=15.0)

                    channel = self.client.get_channel(arg2.id)
                    new_embed = discord.Embed(title=":tada: РОЗЫГРЫШ :tada:",
                                              description=f"**Нажмите на реакцию, чтобы участвовать.**\n\n**Приз:** {args}\n**Время розыгрыша:** {arg1} секунд")
                    message = await channel.send(embed=new_embed)
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
                    Embed_Win = discord.Embed(title="<a:dCongrats:731079711815630901> ПОБЕДИТЕЛЬ "
                                                    "<a:dCongrats:731079711815630901>",
                                              color=discord.Color.blue(),
                                              description=f"{winner.mention} выиграл **{args}**!")
                    await channel.send(embed=Embed_Win)

            else:
                error_embed = discord.Embed(title="Ошибка", color=discord.Color.red(),
                                            description="У вас недостаточно прав")
                await ctx.message.delete(delay=1.0)
                await ctx.send(embed=error_embed, delete_after=5.0)

        except ValueError:
            error_embed = discord.Embed(title="Ошибка", color=discord.Color.red(), description="Неправильный тип "
                                                                                               "аргументов")
            await ctx.message.delete(delay=1.0)
            await ctx.send(embed=error_embed, delete_after=5.0)
        except IndexError:
            error_embed = discord.Embed(title="Ошибка", color=discord.Color.red(),
                                        description="Победителей нет, так как никто не участвовал")
            await ctx.send(embed=error_embed)

    @giveaway.error
    async def giveaway_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            error_embed = discord.Embed(title="Ошибка", color=discord.Color.red(),
                                        description='Такого канала нет на данном сервере')
            await ctx.send(embed=error_embed)


# Loading a cog
def setup(bot):
    bot.add_cog(Giveaway(bot))
