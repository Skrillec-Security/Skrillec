from dis import disco
import os, sys, time, discord

from ...discord_utils.embed_msg import *

async def Role(client, role: discord.Role, member: discord.Member = None):
    return await embed(client, "Role", "Role set on {}".format(member))

"""
not done yet
"""
