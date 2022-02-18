import os, sys, time

## Basic Cmds
from ..commands.help import *
from ..commands.invite import *
## Account 
from ..commands.account_cmds.help_acct import *
from ..commands.account_cmds.info import *
## Attack
from ..commands.attack_cmds.attack import *
from ..commands.attack_cmds.help_attack import *
from ..commands.attack_cmds.methods import *
## Tools
from ..commands.tools_cmds.help_tools import *
from ..commands.tools_cmds.geoip import *
from ..commands.tools_cmds.pscan import *
## ANSI
from ..commands.ansi_cmds.gradient import *
## Mod
from ..commands.mod_cmds.clear import *
from ..commands.mod_cmds.help_mod import *
from ..commands.mod_cmds.purge import *
from ..commands.mod_cmds.role import *
from ..commands.mod_cmds.ban import *

async def handle_cmd(client, msg: str, cmd: str, args):
    # Help Commands
    if cmd == "help" and len(msg) == 5: await help(client)
    elif cmd == "help" and args[1] == "mod": await help_mod(client)
    elif cmd == "invite": await invite_me(client)

    ## Account Commands
    elif cmd == "help" and args[1] == "acct": await help_acct(client)
    elif cmd == "info": await Info(client)

    ## Moderation Commands
    elif cmd == "clear": await clear(client)
    elif cmd == "purge": await purge(client, args)
    #elif cmd == "role": await role(client, args)
    elif cmd == "ban": await ban(client, args)
    # elif cmd == "kick":
    # elif cmd == "lock_channel":
    # elif cmd == "lock_server":

    ## Tools Commands
    elif cmd == "help" and args[1] == "tools": await help_tools(client)
    elif cmd == "geoip": await GeoIP(client, args)
    elif cmd == "pscan": await PortScan(client, args)

    ## DDOS Commands
    elif cmd == "help" and args[1] == "attack": await help_attack(client, args)
    elif cmd == "attack": await attack(client, msg, cmd, args)
    elif cmd == "methods": await methods(client)

    ## ANSI Commands

    elif cmd == "fade": await gradient(client, args)
