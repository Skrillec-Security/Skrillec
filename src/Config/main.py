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
        embed=discord.Embed(title=name, description=description, color=discord.Color.red())
        await client.channel.send(embed=embed)
