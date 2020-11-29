import discord
from discord.ext import commands


class Dev(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command(name="reload", aliases=["r"])
    async def reload(self, ctx, *, cog):
        try:
            self.client.reload_extension(cog)
            await ctx.message.add_reaction("👍")
            print("Reloaded cog:", cog)
        except:
            await ctx.message.add_reaction("👎")


def setup(bot):
    bot.add_cog(Dev(bot))
