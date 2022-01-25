import os, sys, time

from ...discord_utils.embed_msg import *

async def help_mod(client):
    mod_list = """```  Usage       Tools
____________________________________
  purge       Delete an amount of msgs
  clear       Clear's Channel
  kick        Kick User
  ban         Ban User
  unban       Unban User```"""
    await embed(client, "Moderation Commands", mod_list)
