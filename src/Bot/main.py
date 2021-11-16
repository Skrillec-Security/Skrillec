import discord
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

    async def on_message(self, msg):
        full_msg = msg.content
        msg_args = msg.content.split(" ")
        # msg_args = msg_args.replace("")
        if msg.author == self.user:
            return

        """
        Help Command
        """
        if full_msg == "{}help".format(prefix): await msg.channel.send("```{}```".format(Help_CMDs))

        if full_msg.startswith("{}help".format(prefix)) and msg.content != "{}help".format(prefix):
            if len(msg_args) > 1:
                if msg_args[1] == "mod" or msg_args[1] == "moderation":
                    ## show moderation list
                    await msg.channel.send("```{}```".format(moderation_cmds))
                elif msg_args[1] == "iptools":
                    ## show iptools list
                    await msg.channel.send("g")
                elif msg_args[1] == "ascii":
                    await msg.channel.send("")
                elif msg_args[1] == "admin":
                    await msg.channel.send("")

        if full_msg.startswith("{}ban".format(prefix)) and msg.content != "ban":
            await Ban_Syetem(msg, msg_args[1], "")

        """
        Clear Command
        """
        if "clear" in msg.content:
            if len(msg_args) == 1:
                await msg.channel.send("[x] Invalid argument\nUsage: clear <amount>")
            else:
                await msg.channel.purge(limit = int(msg_args[1]))

        """
        My User Info Command
        """
        print(msg.content)
        
