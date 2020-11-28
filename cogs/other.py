import discord
from discord.ext import commands


class Other(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    # This command sends bot invite link
    @commands.command(name="invite")
    async def invite(self, ctx):
        invite_link = discord.Embed(title="Durate Bot", color=0x62FD2A,
                                    description=f"**Спасибо, что выбрали меня!** :heartbeat:\n\nЧтобы пригласить бота "
                                                f"к себе на сервер, нажмите [сюда]( "
                                                f"https://discordapp.com/oauth2/authorize?client_id=637750757319245835"
                                                f"&scope=bot&permissions=805314622)")
        await ctx.send(embed=invite_link)

    # This command sends a link on support server
    @commands.command(name="support")
    async def support(self, ctx):
        server = discord.Embed(title="Сервер поддержки", color=0x562FAD,
                               description="Чтобы вступить на сервер поддержки бота, нажмите [сюда]("
                                           "https://discord.gg/RQPZZzA)")
        await ctx.send(embed=server)


# Loading a cog
def setup(bot):
    bot.add_cog(Other(bot))
