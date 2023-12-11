import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE3NzY3ODA2MDc2NjY0MjMwNw.GCBGLK.chH-Wh-hmPoj3D56B3xSYaaoCrAj1XrfUfD7kg')


