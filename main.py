import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run('NjM3NzUwNzU3MzE5MjQ1ODM1.XbSttA.FwgfcNENFVZZognRtynzzPeoArI')