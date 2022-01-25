import os, sys, time, discord

from ...discord_utils.embed_msg import *

async def help_acct(client):
    acct_cmds = """```  Usage       Tools
____________________________________
  register    Register for Attack System
  info        Account plan
  redeem      Redeem a toke```"""
    return await embed(client, "Account Commands", acct_cmds)