import os, sys, time, requests, discord

# Importing submodules
from src.bot.command_handler import *
from src.config.main import *
from src.config.config_cmds import *
from src.config.configure import *
from src.discord_utils.embed_msg import *
from src.utils.custom_utils import *
from src.blacklist.main import *

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_join(self, client):
        if client.author.id in BlacklistedUsers():
            await client.create_dm.send("You're a broke fucking skid. Stop trying to join random")
            await client.delete()
            await client.kick()

    async def on_message(self, client):
        if url_block(client.content) == 0 | client.author.id != "918258241576792115":
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

client = MyClient()
python_is_gay_as_fuck = str(Configuration.get_token())
client.run('OTMxOTQ4MTUwNzk5ODcyMDQw.YeL2WQ.dgL122UDEptrILE73A-K_BQomLk')
