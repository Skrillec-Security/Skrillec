import os, sys, time

from ...authentication.crud import *
from ...discord_utils.embed_msg import *

async def Info(client):
    info = Crud.find_user(str(client.author.id))
    output = """```[User]: {0}, {1}
[Level]: {2}
[Max time]: {3}
[Concurrent]: {4}
[Ongoing]: {5}
[Admin]: {6}
[Expiry]: {7}```""".format(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7])
    await embed(client, "User Information", output)