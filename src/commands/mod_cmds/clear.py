import os, sys, time, discord

from ...discord_utils.embed_msg import *

async def clear(client):
    edit_pos = await client.channel.clone()
    await client.channel.delete()
    await edit_pos.edit(position=client.channel.position, sync_permission=True)
