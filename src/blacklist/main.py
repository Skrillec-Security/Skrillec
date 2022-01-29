import os, sys, time

from ..config.main import *

class Blacklist:
    async def Users():
        print(open(Config.local_blacklist_path_backup, "r").read().split("\n"))
        return open(Config.local_blacklist_path_backup, "r").read().split("\n")

    """
        Use example:

            err_check = add_user(34324234)
            if err_check == 0 | err_check -1:
                ## Handle here
    """
    def add_user(userid):
        try:
            db = open(Config.local_blacklist_path, "a")
            db.write(userid)
            db.close()
            return 1 ## User Added Worked
        except:
            return -1 ## Error
        return 0 ## Didnt work


    # def remove_user(userid):

