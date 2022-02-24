import os, sys, time, discord

from ...discord_utils.embed_msg import *

async def clock(client):
	for ch in client.guild.channels:
		await ch.set_permissions(client.guild.default_role, send_messages=False)

	await embed(client, "Successfuly lock channel!", "all channels have been locked!!")
