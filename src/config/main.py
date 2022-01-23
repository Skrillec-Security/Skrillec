import os, sys, time
# Import Submodules (Commands)
from ..commands.help import *
from ..commands.clear import *

class Config:
    local_db_path_backup = os.getcwd() + "\\src\\db\\users.skrillec"
    local_db_path = os.getcwd() + "/src/db/users.skrillec"
    local_api_path = os.getcwd() + "/src/db/apis.skrillec"
    local_cmdlog_db_path = os.getcwd() + "/src/logs/command.log"
    local_settings_path = os.getcwd() + "/src/settings.skrillec"
    bot_prefix = ";"