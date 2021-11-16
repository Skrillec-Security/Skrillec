import sys, os, time, discord

from ...Config.main import *

async def Help(client, fmsg, msg_args):
    if len(msg_args) > 1:
        if msg_args[1] == "mod" or msg_args[1] == "moderation":
            ## show moderation list
            await client.channel.send("```{}```".format(Config.Moderation_CMDs))
        elif msg_args[1] == "iptools":
            ## show iptools list
            await client.channel.send("g")
        elif msg_args[1] == "ascii":
            await client.channel.send("")
        elif msg_args[1] == "admin":
            await client.channel.send("")