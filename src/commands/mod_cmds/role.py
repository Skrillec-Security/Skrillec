import os, sys, time

from ...discord_utils.embed_msg import *

async def Role(client, args):
    return await embed(client, "Role", "Role set on ")