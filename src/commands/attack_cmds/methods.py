import os, sys, time
from ...discord_utils.embed_msg import *

async def methods(client):
    methods_list = """• home
• dvr
• openvpn2
• wsd
• snmp
• ovh-gb
• ovh-drown
• ovh-acid
• ovh-udp
• 100up-acid
• cpu
• 22-ssh
• nfo-acid
• nfo-ssh
• syn-star
• ack-star
• tempest-acid
• psn-rape
• server-uwsi
• udpbypass-v2
• udp-v1
• vpn-mix-v3
• ark-255
• ark-lift
• rust-game
• fivem-bypass
• syn-vr
• std-vr"""
    await embed(client, "Methods", methods_list)