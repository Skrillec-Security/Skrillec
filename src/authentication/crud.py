from collections import UserString
import os, sys, time

from ..config.main import *
from .crud import *

class Crud:
    def parse_dbLine(line):
        return ((line.replace("('", "")).replace("')", "")).split("','")

    def find_user(userid):
        try:
            users = open(Config.local_db_path, "r").read()
            for user in users.split("\n"):
                if len(user) == 0: return 0
                info = Crud.parse_dbLine(user)
                # print("DB ID Pulled: " + info[1] + " | " + str(userid)) ##debug test
                if info[1] == str(userid):
                    return info
        except:
            return -1
        return 0

    def register_user(discord_name, discord_id):
        try:
            users_db = open(Config.local_db_path, "a")
            users_db.write("('" + discord_name + "','" + discord_id + "','0','0','0','0','0','0/0/0000")
            users_db.close()
            return 1
        except:
            return -1
        return 0

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

    def update_user(userid, new_lvl, new_mtime, new_conn, new_admin, new_expiry) -> bool:
        new_db = ""
        try: ## Adding a try/except to handle errors instead of exiting app with an error 
            users = open(Config.local_db_path, "r").read().split("\n") ## Reading file and splitting the file data into "\n" (Lines)
            for user in users: ## Looping thru lines in the file
                if len(user) == 0 | len(user) < 15: continue ## Skip empty/un-necessary lines 
                info = Crud.parse_dbLine(user) ## Parsing the line into an array
                if info[1] == userid: ## looking for user line in file
                    new_db += "('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')\n".format(info[0], userid, new_lvl, new_mtime, info[4], new_conn, new_admin, new_expiry)
                else:
                    new_db += user ## Putting the other lines back in file
            return "[+] User <@{0}> updated!".format(userid)
        except:
            return "[x] Exception Error, Unable to update user!"
            
