import discord
from discord import client
class Config:

    Bot_Info = {
        "Title": "Skrillec",
        "Description": "The 2022 New All-In-One Moderation. Eliminating the usage of multiple bots with limited commands on each",
        "Version": "1.00",
        "Prefix": ">"
    }

    Current = {
        "fullmsg": "",
        "cmd": "",
        "args": [],
    }

    Help_CMDs = r"""List Of Commands
________________________________________________
>Help Moderation | List Of Moderation Commands
>Help IPTools | List Of IP/Networking Tools
>Help ASCII | List of ASCII/ANSI Convertion Tools
>Help Admin | List of Skrillec admin commands"""

    Moderation_CMDs = r"""List Of Moderation Commands
_______________________________________
>clear <amount> | Clear Messages
>ban <user> <reason> | Ban A User"""

    ansi_CMDs = r""" """

    async def embed(name,description,client):
        embed=discord.Embed(title=name, description=description, color=discord.Color.blurple())
        await client.channel.send(embed=embed)
    
    async def Help_CMD(client):
        help = discord.Embed(title='List Of Commands', color=discord.Color.dark_purple())
        help.add_field(name='>help mod', value='A list of Moderation Commands.', inline=False)
        help.add_field(name='>help IPTools', value="A list of IP/Networking tools.", inline=False)
        help.add_field(name='>help ASCII', value='a list of ASCII/ANSI convertion tools.', inline=False)
        help.add_field(name='>help admin', value='A list of Skrillec Admin Commands.', inline=False)
        help.set_footer(text='{} | Prefix: {} | Version: {}'.format(Config.Bot_Info['Title'], Config.Bot_Info['Prefix'], Config.Bot_Info['Version']))
        await client.channel.send(embed=help)

    async def Mod_CMD(client):
        modList = discord.Embed(title='The Moderation Commands', color=discord.Color.dark_purple())
        modList.add_field(name='>clear <amount>', value="clears messages", inline=False)
        modList.add_field(name='>ban <user>', value='bans a user', inline=False)
        modList.add_field(name='>kick <user>', value='kicks a user', inline=False)
        await client.channel.send(embed=modList)

