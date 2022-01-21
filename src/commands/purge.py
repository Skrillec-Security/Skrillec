import os, sys, time

from ..discord_utils.embed_msg import *
from ..config.main import *

async def purge(client, args):
    try:
        int(args[1])
    except:
        return await embed(client, "Error", "You did not provide a valid number!")
    if int(args[1]) > 500: return await embed(client, "Error", "You provided a number over the maximum of messages i can delete!. Use " + Config.bot_prefix + "clear to completely clear the channel!")
    await client.channel.purge(limit=int(args[1]))