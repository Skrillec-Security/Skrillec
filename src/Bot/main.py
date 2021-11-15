import discord
from .Commands.ban import *
from ..Config.main import *


Help_CMDs = r""">Help Moderation | List Of Moderation Commands
>Help IPTools | List Of IP/Networking Tools
>Help ASCII | List of ASCII/ANSI Convertion Tools
>Help Admin | List of Skrillec admin commands
    """
moderation_cmds = ">"

class Skrillec(discord.Client):
    async def on_ready(self):
        print("\nbot has started")

    async def on_message(self, msg):
        full_msg = msg[1:]
        msg_args = msg.content.split(" ")
        msg_args = msg_args.replace("")
        if msg.author == self.user:
            return

        """
        Help Command
        """
        if msg.content == "help": await msg.channel.send("```{}```".format(Help_CMDs))

        if "help" in msg.content and msg.content != "help":
            if len(msg_args) > 1:
                if msg_args[1] == "mod" or msg_args[1] == "moderation":
                    ## show moderation list
                    await msg.channel.send(moderation_cmds)
                elif msg_args[1] == "iptools":
                    ## show iptools list
                    await msg.channel.send("g")
                elif msg_args[1] == "ascii":
                    await msg.channel.send("")
                elif msg_args[1] == "admin":
                    await msg.channel.send("")

        if "ban" in msg.content and msg.content != "ban":
            await Banner_Syetem(msg, "", 0)

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
        
