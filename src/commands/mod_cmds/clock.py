import os, sys, time, discord

from ...discord_utils.embed_msg import *

async def clock(client):
    await client.channel.send("Locking Channel")

async def create_lcok_role(ctx, *, ChannelLock):
	guild = ctx.guild
	await guild.create_role(name=ChannelLock)

'''
not done yet
'''
