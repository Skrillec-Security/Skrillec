
"""
    Discord.py Blacklist Module

    This module blacklist a users ID and errors them upon joining server or trying to use 
    the bot in another server. 

    To avoid error spam when user try using the bot. Nothing will happen besides deleting msg

"""
import os, sys, time

from .config.main import *

async def blacklist_user(client, args):
    return ""