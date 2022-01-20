import os, sys, time

from ..config.main import *

def parse_dbLine(line):
    return ((line.replace("('", "")).replace("')", "")).split("','")

def find_user(userid):
    try:
        users = open(Config.local_db_path, "r").read()
        for user in users.split("\n"):
            if len(user) == 0: return 0
            info = parse_dbLine(user)
            # print("DB ID Pulled: " + info[1] + " | " + str(userid)) ##debug test
            if info[1] == str(userid):
                return info
    except:
        return 0
    return 0

def register_user(discord_name, discord_id):
    try:
        users_db = open(Config.local_db_path, "a")
        users_db.write("('" + discord_name + "','" + discord_id + "','0','0','0','0','0','0/0/0000")
        users_db.close()
    except:
        return 0
    return 1

def remove_user(discord_id):
    try:
        users_db = open(Config.local_db_path, "r").read()
        new_db = ""
        for user in users_db:
            if user.contains("','" + discord_id + "','"): continue
            else: new_db += user + "\n"
        r = open(Config.local_db_path, "a")
        r.write(new_db)
        r.close()
    except:
        return 0
    return 1
