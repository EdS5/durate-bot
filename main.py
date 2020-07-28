import discord
from discord.ext import commands
import os



client = commands.Bot(command_prefix = '!')
client.remove_command("help")
__version__ = "0.3"



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



token = os.environ.get('BOT_TOKEN')
client.run(str(token))
