import os, sys, time, requests

from ...discord_utils.embed_msg import *


async def GeoIP(client, args):
    print("getting here")
    test = ((requests.get("http://ip-api.com/json/" + args[1]).text).replace("\",\"", "\r\n")).replace("\":\"", ": ").replace("{\"", "").replace("\"}", "").replace("\":", ": ").replace(",\"", "\r\n")
    print(test)
    return(await embed(client, "GeoIP", "```{}```".format(test)))
