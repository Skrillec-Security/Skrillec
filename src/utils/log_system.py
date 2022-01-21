import os, sys, time

from ..config.main import *

class Logger: 
    def new_log(discord_name, discord_id, args):
        ## Current Time
        log_formart = """
[User]: 
        """
        cmd_db = open(Config.local_cmdlog_db_path, "a")
        cmd_db.write("")