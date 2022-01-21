import os, sys, time, discord

from ..discord_utils.embed_msg import *
from ..config.main import *

async def role(client, args):
    if len(args) < 1: return (await embed(client, "Error", "[x] Invalid argument. " + Config.bot_prefix + "role <userid>"))
    memberid = args[1].replace("<@!", "").replace(">", "")
    role = discord.utils.get(client.guild.roles, name=args[2])
    member = client.guild.get_member(int(memberid))
    member.add_roles(role)
    # print(str(client.guild.roles))
    # for i in client.guild.roles:
    #     print(str(i.id) + " | " + str(i.name))

    # for c in client.guild.members:
    #     print(c)
