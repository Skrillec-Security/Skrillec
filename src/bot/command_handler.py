import os, sys, time

from ..commands.help import *
from ..commands.clear import *
from ..commands.help_mod import *
from ..commands.attack import *

async def handle_cmd(client, msg: str, cmd: str, args):
    # Help Commands
    if cmd == "help": await help(client)
    elif cmd == "help" and rgs[1] == "mod": await help_mod()

    ## Moderation Commands
    elif cmd == "clear": await clear(client)
    elif cmd == "purge": await purge(client)
    # elif cmd == "ban": 
    # elif cmd == "kick":
    # elif cmd == "lock_channel":
    # elif cmd == "lock_server":

    ## DDOS Commands
    elif cmd == "attack": await attack(client, msg, cmd, args)
