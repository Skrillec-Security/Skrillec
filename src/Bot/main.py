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

class Skrillec(discord.Client):
    async def on_ready(self):
        print("\nbot has started")

    async def on_message(self, client):
        full_msg = client.content
        msg_args = client.content.split(" ")
        # msg_args = msg_args.replace("")
        if client.author == self.user:
            return

        if full_msg == "{}home".format(prefix): await client.channel.send("Coming soon....")
        if full_msg == "{}help".format(prefix): await client.channel.send("```{}```".format(Config.Help_CMDs))

        elif full_msg.startswith("{}help".format(prefix)) and client.content != "{}help".format(prefix):
            await Help(client, full_msg, msg_args)

        elif full_msg.startswith("{}ban".format(prefix)) and client.content != "ban":
            await Ban_Syetem(client, full_msg, msg_args)

        # elif "clear" in client.content:
        #     await Clear_System(client, full_msg, msg_args)

        print(client.content)
        
