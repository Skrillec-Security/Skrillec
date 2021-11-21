import os, sys, time, discord

from .main import *

class Configuration:
    async def Configure_MSG_Info(client):
        Config.Current["fullmsg"] = client.content
        Config.Current['args'] = ["", ""]
        if " " in client.content:
            Config.Current['args'] = (client.content).split(" ")
            Config.Current["cmd"] = Config.Current['args'][0].replace(Config.Bot_Info['Prefix'], "")
        else:
            Config.Current['args'].append(client.content)
            Config.Current['cmd'] = (client.content).replace(Config.Bot_Info['Prefix'], "")
