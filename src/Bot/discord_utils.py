from ..Config.main import *
import discord

class discordUtils:
    async def send_Message(client, Title, Description):
        embed = discord.Embed(title=Title, description=Description, color=discord.Color.red())
        await client.channel.send(embed=embed)

    async def error_Message(client, desc):
        error = discord.Embed(description=desc, color= discord.Color.from_rgb(252,3,3))
        error.set_footer(text='{} | Prefix: {} | Version: {}'.format(Config.Bot_Info['Title'], Config.Bot_Info['Prefix'], Config.Bot_Info['Version']))
        await client.channel.send(embed=error)
