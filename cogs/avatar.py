import discord
from discord.ext import commands


class Avatar(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command(pass_context=True, name="avatar")
    async def avatar(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        show_avatar = discord.Embed(description="[Открыть в браузере](%s)" % member.avatar_url,
                                    color=discord.Color.blue())
        show_avatar.set_image(url="{}".format(member.avatar_url))
        show_avatar.set_footer(text=f'{member}')
        await ctx.send(embed=show_avatar)


def setup(bot):
    bot.add_cog(Avatar(bot))
