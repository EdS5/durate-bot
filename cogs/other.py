import discord
from discord.ext import commands


class Other(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command(name="invite")
    async def invite(self, ctx):
        invlink = discord.Embed(title="Durate Bot", color=0x359475,
                                description=f"**Спасибо, что выбрали меня!** :heartbeat:\n\nЧтобы пригласить бота к себе на сервер, нажмите [сюда](https://discordapp.com/oauth2/authorize?client_id=637750757319245835&scope=bot&permissions=805314622)")
        await ctx.send(embed=invlink)


    @commands.command(name="support")
    async def support(self, ctx):
        server = discord.Embed(title="Сервер поддержки", color=0x562FAD,
                               description="Чтобы вступить на сервер поддержки бота, нажмите [сюда](https://discord.gg/7nnGaKW)")
        await ctx.send(embed=server)


def setup(bot):
    bot.add_cog(Other(bot))