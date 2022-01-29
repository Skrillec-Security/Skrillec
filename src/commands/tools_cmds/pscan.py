import os, sys, time, requests

from ...discord_utils.embed_msg import *

async def PortScan(client, args):
    if len(args) < 1: return (await embed(client, "Error", "[x] Error, Invalid argument\nUsage: ;pscan <ip>\nExample: ;psan 1.1.1.1"))
    ports = requests.get("https://api.skrillec.pw/pscan.php?q={0}".format(args[1])).text
    await embed(client, "Port Scan Results", "```" + ports.replace("</br>", "") + "```")