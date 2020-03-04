import discord
from discord.ext import commands

TOKEN = 'Njg0NTMxMjA4NTQxMDQ0NzQz.Xl7dsA.OGLRmAS9xnBQ8MpJpKtXpFYTjy4'

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('🚚 Vendor Nederland Truckers'))
    print('Bot is ready.')

client.run(TOKEN)
