import os, sys, time

from ...authentication.crud import *
from ...discord_utils.embed_msg import *

async def Register(client):
    username = client.author.name
    user_id = client.author.id
    Crud.register_user(username, user_id)
    await embed(client, "successfully registered!", "Username: {0}\nUser ID     : {1}".format(username, user_id))
