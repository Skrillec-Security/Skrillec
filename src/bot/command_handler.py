import os, sys, time

from ..commands.help import *
from ..commands.clear import *
from ..commands.help_mod import *
from ..commands.attack import *
from ..commands.purge import *
from ..commands.role import *
from ..commands.attack import *
from ..commands.info import *
from ..commands.help_attack import *
from ..commands.methods import *

async def handle_cmd(client, msg: str, cmd: str, args):
    # Help Commands
    if cmd == "help" and len(msg) == 5: await help(client)
    elif cmd == "help" and args[1] == "mod": await help_mod(client)

    ## Account Commands
    elif cmd == "info": await Info(client)

    ## Moderation Commands
    elif cmd == "clear": await clear(client)
    elif cmd == "purge": await purge(client, args)
    elif cmd == "role": await role(client, args)
    # elif cmd == "ban": 
    # elif cmd == "kick":
    # elif cmd == "lock_channel":
    # elif cmd == "lock_server":

    ## DDOS Commands
    elif cmd == "help" and args[1] == "attack": await help_attack(client, args)
    elif cmd == "attack": await attack(client, msg, cmd, args)
    elif cmd == "methods": await methods(client)
