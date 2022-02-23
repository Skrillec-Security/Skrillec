import os, sys, time

from ...authentication.crud import *
from ...discord_utils.embed_msg import *

async def Info(client):
    info = Crud.find_user(str(client.author.id))
    try:
        if info == 0 | info == -1:
            return (await embed(client, "Info Error", "You are not registered. Type `{}register` in order to register!"))
    except:
        output = "```[User]: {0}, {1}\n[Level]: {2}\n[Max time]: {3}\n[Concurrent]: {4}\n[Ongoing]: {5}\n[Admin]: {6}\n[Expiry]: {7}```".format(str(info[0]), str(info[1]), str(info[2]), str(info[3]), str(info[4]), str(info[5]), str(info[6]), str(info[7]))
    return await embed(client, "User Information", output)
