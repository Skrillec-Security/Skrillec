import os, sys, time, discord

from ...discord_utils.embed_msg import *

async def help_acct(client):
    await EmbedMessages.Acct_Menu(client)