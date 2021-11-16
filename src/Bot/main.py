"""
@title: Skrillec Advanced Bot
@authors: Occupied, satisfied
@since: 11/14/21
""" 
import discord
from .Commands.help import *
from .Commands.clear import *
from .Commands.ban import *
from ..Config.main import *

prefix = ">"
Help_CMDs = r"""List Of Commands
________________________________________________
>Help Moderation | List Of Moderation Commands
>Help IPTools | List Of IP/Networking Tools
>Help ASCII | List of ASCII/ANSI Convertion Tools
>Help Admin | List of Skrillec admin commands"""

moderation_cmds = r"""List Of Moderation Commands
_______________________________________
>clear <amount> | Clear Messages
>ban <user> <reason> | Ban A User"""

class Skrillec(discord.Client):
    async def on_ready(self):
        print("\nbot has started")

    async def on_message(self, client):
        full_msg = client.content
        msg_args = client.content.split(" ")
        # msg_args = msg_args.replace("")
        if client.author == self.user:
            return

        """
        Help Command
        """
        if full_msg == "{}help".format(prefix): await client.channel.send("```{}```".format(Help_CMDs))

        elif full_msg.startswith("{}help".format(prefix)) and client.content != "{}help".format(prefix):
            Help(client, full_msg, msg_args)

        elif full_msg.startswith("{}ban".format(prefix)) and client.content != "ban":
            await Ban_Syetem(client, full_msg, msg_args)

        elif "clear" in client.content:
            await Clear_System(client, full_msg, msg_args)

        print(client.content)
        
