import os, sys, time, discord

from ...config.main import *
from ...discord_utils.embed_msg import *


async def mute(client, args):
    if len(args) < 1: return (await embed(client, "Mute Error", "[x] Invalid argument\nUsage: {0}mute <userid/@tag>"))

    userid = args[1].replace("<@", "").replace(">", "").replace("!", "")
    member = await client.guild.fetch_member(userid)
    role = discord.utils.get(client.guild.roles, name="muted")
    await member.add_roles(role)
    return (await embed(client, "Mute User", "<@{0}> has been muted!".format(userid)))