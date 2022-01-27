import os, sys, time

from ..config.main import *

class Blacklist:
    def BlacklistedUsers():
        return open(Config.local_blacklist_path, "r").read().split("\n")

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

