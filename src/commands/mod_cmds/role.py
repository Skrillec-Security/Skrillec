from dis import disco
import os, sys, time, discord

from ...discord_utils.embed_msg import *

async def Role(client, args):
    if len(args) < 1:
        return (await embed(client, "Error", "Invalid argument\nUsage: {}role <userid/@tag> <role/@tag>"))

    userid = args[1]
    role = args[2]

    ## Filtering discord tag on user tag or role tag
    userid = userid.replace("<@", "").replace(">","").replace("!","")
    role = role.replace("<@", "").replace(">", "").replace("&", "")

    user = await client.guild.fetch_member(userid)
    role = discord.utils.get(client.guild.roles, name=str(role))

    await user.add_roles(role)
    return await embed(client, "Role", "Role set on <@{}>".format(userid))

"""
not done yet
"""
