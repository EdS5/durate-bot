import discord
from discord.ext import commands
import random


class Ball(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command(name="8ball")
    async def _8ball(self, ctx, *, args=None):
        responses = ('Да :white_check_mark:',
                     'Нет :x:',
                     'Возможно',
                     'Никак нет :name_badge:')

        embed = discord.Embed(title='Волшебный шар', colour=discord.Colour.purple())
        embed.add_field(name="**Вопрос:**", value=args)
        embed.add_field(name="**Ответ:**", value=f"{random.choice(responses)}")
        embedError = discord.Embed(title="Ошибка", description="Не были введены аргемуенты")
        embedLenError = discord.Embed(title="Ошибка", description="Введите текст меньше 1024 символов")
        if args is None:
            await ctx.send(embed=embedError)
            return
        if args is not None:
            if len(args) >= 1024:  # Discord limits
                await ctx.send(embed=embedLenError)
                return
        await ctx.send(embed=embed)


# Loading a cog
def setup(bot):
    bot.add_cog(Ball(bot))
