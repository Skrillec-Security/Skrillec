import os, sys, time

from ..discord_utils.embed_msg import *

async def invite_me(client):
    await embed(client, "Invite me", "Invite me to your server!\n\n```https://discord.com/api/oauth2/authorize?client_id=943994801752244334&permissions=8&scope=bot```")