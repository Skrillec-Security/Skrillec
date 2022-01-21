import os, sys, time, requests, discord

# Importing submodules
from src.bot.command_handler import *
from src.config.main import *
from src.config.config_cmds import *
from src.utils.embed_msg import *

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, client):
        # if client.author.tag == self.user: return
        if (client.content).startswith(Config.bot_prefix):
            ## Look for command in 'src/commands/' folder!
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

client = MyClient()
client.run('OTMxOTQ4MTUwNzk5ODcyMDQw.YeL2WQ.sjA4i-912yWZDmHCz7_pkS7AvdY')
