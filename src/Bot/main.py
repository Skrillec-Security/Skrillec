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

        if full_msg.startswith("{}help".format(prefix)) and client.content != "{}help".format(prefix):
            if len(msg_args) > 1:
                if msg_args[1] == "mod" or msg_args[1] == "moderation":
                    ## show moderation list
                    await client.channel.send("```{}```".format(moderation_cmds))
                elif msg_args[1] == "iptools":
                    ## show iptools list
                    await client.channel.send("g")
                elif msg_args[1] == "ascii":
                    await client.channel.send("")
                elif msg_args[1] == "admin":
                    await client.channel.send("")

        if full_msg.startswith("{}ban".format(prefix)) and client.content != "ban":
            await Ban_Syetem(client, full_msg, msg_args)

        """
        Clear Command
        """
        if "clear" in client.content:
            if len(msg_args) == 1:
                await client.channel.send("[x] Invalid argument\nUsage: clear <amount>")
            else:
                await client.channel.purge(limit = int(msg_args[1]))

        """
        My User Info Command
        """
        print(client.content)
        
