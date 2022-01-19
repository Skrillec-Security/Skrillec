import os, sys, time
from ..Config.main import *

def find_user(userid):
    try:
        users = open(Config.local_db_path, "r").split("\n")
        for user in users:
            if user.contains("','{}','".format(userid)):
                info = ((user.replace("('", "")).replace("')", "")).split(" ")
                return info
    except:
        return 0
    return 0

def register_user(discord_name, discord_id):
    try:
        users_db = open(Config.local_db_path, "a")
        users_db.write(f"('{}','{}','0','0','0','0','0','0/0/0000".format(discord_name, discord_id))
        users_db.close()
    except:
        return 0
    return 1