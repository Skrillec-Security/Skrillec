import os, sys, time, discord

from ...discord_utils.embed_msg import *

async def clock(client):
	for ch in client.guild.channels:
		await ch.set_permissions(client.guild.default_role,  read_messages=True, send_messages=False)
	
	await embed(client, "Successfuly lock channel!", "all channels have been locked!!")
