
"""
    Jeff the eGod here,
"""
import os, sys, time, requests, discord, threading

intents = discord.Intents.default()
intents.members = True

# Importing submodules
from src.bot.command_handler import *
from src.config.main import *
from src.config.config_cmds import *
from src.config.configure import *
from src.discord_utils.embed_msg import *
from src.utils.custom_utils import *
from src.blacklist.main import *


"""
    Skrillec Moderation Bot
"""

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_join(self, client):
        print("works 1")
        
    async def on_member_join(self, client):
        print("works 2")

    async def on_message(self, client):
        if url_block(client.content) == 0:
            await client.delete()
            return await embed(client, "Error", "No Links Skid")
        if (client.content).startswith(Config.bot_prefix):
            full_cmd = client.content
            cmd_args = (client.content).split(" ")
            cmd = (cmd_args[0])[1:]
            print(cmd)

            all_cmds = get_cmds()
            if cmd in all_cmds:
                await handle_cmd(client, full_cmd, cmd, cmd_args)
            else:
                await embed(client, "Error", "Command not found!")



        print('client from {0.author}: {0.content}'.format(client))


"""
    Skrillec DDOS Bot
"""
class Skrillec_DDOS(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, client):
        print('client from {0.author}: {0.content}'.format(client))

client = MyClient(intents=intents)
client.run(sys.argv[1])
