import os, sys, time
from ...discord_utils.embed_msg import *

async def methods(client):
    methods_list = """LKZ-GET
LKZ-POST
LKZ-HEAD
LKZ-FIVEM
LKZ-TCPBYPASS
LKZ-NTP
LKZ-OVHBETA
LKZ-KILLALL
LKZ-ICMP
LKZ-HOME
LKZ-VSE
LKZ-GAMEV2
LKZ-SYNBYPASS
LKZ-UDPBYPASS
LKZ-DNS
LKZ-NFO
LKZ-FIVEMTCP
LKZ-OVHBETAV2
LKZ-TCPEXTRA
LKZ-OVHV4"""
    methods_list2 = """HOME-TRC
TCP-TRC
SSH-TRC
NFO-TRC
OVH-TRC
GAME-TRC
FIVEM-TRC
ARK-TRC
RUST-TRC
MC-TRC
HTTPS-TRC"""
    await embed(client, "API 1 Methods", "```{0}```".format(methods_list))
    await embed(client, "API 2 Methods", "```{0}```".format(methods_list2))