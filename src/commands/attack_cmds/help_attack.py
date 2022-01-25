import os, sys, time

from ...discord_utils.embed_msg import *

async def help_attack(client, args):
    attack_list = """```
  Usage       Tools
____________________________________
  register    Register 
  account     Account/Plan Info
  methods     List of Methods
  attack      Stresser
    ```"""
    await embed(client, "Attack Commands", attack_list)