import os, sys, time

from ..config.main import *

async def stress(client, fmsg, cmd, args):
    if len(args) < 4: return (await client.channel.send("[x] Error, Invalid argument\nUsage {}stress <ip> <port> <time> <method>\nExample: {}stress 1.1.1.1 80 300 UDP".format(Config.bot_prefix, Config.bot_prefix)))
    await client.channel.send("works")