from ..Config.main import *
import discord

class discordUtils:
    async def send_Message(client, Title, Description):
        embed = discord.Embed(title=Title, description=Description, color=discord.Color.red())
        embed.set_footer(text='{} | Prefix: {} | Version: {}'.format(Config.Bot_Info['Title'], Config.Bot_Info['Prefix'], Config.Bot_Info['Version']))
        await client.channel.send(embed=embed)

#ERROR EMBED
    async def error_Message(client, desc):
        error = discord.Embed(description=desc, color= discord.Color.from_rgb(252,3,3))
        error.set_footer(text='{} | Prefix: {} | Version: {}'.format(Config.Bot_Info['Title'], Config.Bot_Info['Prefix'], Config.Bot_Info['Version']))
        await client.channel.send(embed=error)

#GREEN EMBED / SUCCESS
    async def successful_Message(client, desc):
        success = discord.Embed(description=desc, color= discord.Color.from_rgb(3,252,90))
        success.set_footer(text='{} | Prefix: {} | Version: {}'.format(Config.Bot_Info['Title'], Config.Bot_Info['Prefix'], Config.Bot_Info['Version']))
        await client.channel.send(embed=success)
