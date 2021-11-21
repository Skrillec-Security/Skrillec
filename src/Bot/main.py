"""
@title: Skrillec Advanced Bot
@authors: Occupied, satisfied
@since: 11/14/21
""" 
import discord

from .Commands.help import *
from .Commands.clear import *
from .Commands.ban import *
from .Commands.kick import *

from ..Config.main import *
from ..Config.configure import *

prefix = ">"

class Skrillec(discord.Client):
    async def on_ready(self):
        print("\nbot has started")
        
    async def on_member_join(self, member):
        return "" ##change this shit here

    async def on_message(self, client):
        await Configuration.Configure_MSG_Info(client)
        print("{}".format(Config.Current['fullmsg']))
        if client.author == self.user:
            return

        if Config.Current['fullmsg'] == "{}home".format(prefix): await client.channel.send("Coming soon....")
        # if Config.Current['fullmsg'] == "{}help".format(prefix): await client.channel.send("```{}```".format(Config.Help_CMDs))
        if Config.Current['fullmsg'] == "{}help".format(prefix): await Config.Help_CMD(client)

        elif Config.Current['fullmsg'].startswith("{}help".format(prefix)) and Config.Current['fullmsg'] != "{}help".format(prefix):
            await Help(client, Config.Current['fullmsg'], Config.Current['args'])

        elif Config.Current['fullmsg'].startswith("{}ban".format(prefix)) and Config.Current['fullmsg'] != "ban":
            await Ban_Syetem(client, Config.Current['fullmsg'], Config.Current['args'])

        elif Config.Current['fullmsg'].startswith("{}kick".format(prefix)) and Config.Current['fullmsg'] != "kick":
            await dick(client, Config.Current['fullmsg'], Config.Current['args'])

        # elif "clear" in client.content:
        #     await Clear_System(client, full_msg, msg_args)

        print(Config.Current['fullmsg'])
        
