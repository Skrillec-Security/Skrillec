import os, sys, time

from ..config.main import *
## discord_name, discord_id, server_name, server_id, channel_name, channel_id
class Logger:
    global discord_name
    global discord_id
    global server_name
    global server_id
    global channel_name
    global channel_id

    global log_formatted
    def set_info(dname, did, sname, sid, cname, cid):
        discord_name = dname
        discord_id = did
        server_name = sname
        server_id = sid
        channel_name = cname
        channel_id = sid
        create_format():
        
    def create_format():
        log_format = """
