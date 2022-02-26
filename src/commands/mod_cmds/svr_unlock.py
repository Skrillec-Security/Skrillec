import os, sys, time, discord

from ...discord_utils.embed_msg import *

async def svr_unlock(client):
	for ch in client.guild.channels:
		await ch.set_permissions(client.guild.default_role,  read_messages=True, send_messages=True)
	
	await embed(client, "Successfuly unlock channel!", "Channel unlocked.")
