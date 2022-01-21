import os, sys, time, discord

from ..discord_utils.embed_msg import *

async def help(client):
    help_list = """```  Usage       Tools
____________________________________
  help        All help list
  help mod    Moderation Commands
  help tools  IP/URL Network Tools
  help attack Stresser (Premium)
  help ansi   ANSI/ASCII Tools```"""
    await embed(client, "Help Commands", help_list)