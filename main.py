import discord
from discord.ext import commands



client = commands.Bot(command_prefix = '!')
TOKEN = 'NjM3NzUwNzU3MzE5MjQ1ODM1.XbStrQ._qLJAV3c0xin7BVTGSOz3o5YmvI'
client.remove_command("help")



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="version 0.3 | !help", url="https://www.twitch.tv/eds52", type=discord.ActivityType.watching))
    print("Bot is ready.")


#@client.command(pass_context=True)
#async def case(ctx, arg1=None, arg2=None):
 #   if arg1 == 'open' and arg2 == 'dlore':
#
 #       responses = ['awp басков',
  #                   'егор криг',
   #                  'калаш малахов',
    #                 'дигл пугачёва']
     #   await ctx.send(f'Вам выпало - ***{random.choice(responses)}***')
    #if arg1 is None:
     #   embedNoArg = discord.Embed(title="Ошибка",description="Не были введены аргументы")
      #  await ctx.send(embed=embedNoArg)
   # if arg1 == "open" and arg2 is None:
    #    embedSelectCase = discord.Embed(title="Выберите кейс из доступных")
     #   embedSelectCase.add_field(name="dlore",value="Не включает ничего. буквально")
      #  await ctx.send(embed=embedSelectCase)
   # else:
    #    pass





cogs = {"information", "8ball", "giveaway", "avatar", "moderation", "other"}

for cog in cogs:
    client.load_extension(f"cogs.{cog}")



client.run(TOKEN)