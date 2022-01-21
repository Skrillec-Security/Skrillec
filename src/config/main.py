import os, sys, time
# Import Submodules (Commands)
from ..commands.help import *
from ..commands.clear import *

class Config:
    local_db_path = os.getcwd() + "/src/assets/db/users.skrillec"
    local_cmdlog_db_path = os.getcwd() + "/src/assets/logs/command.log"
    local_settings_path = os.getcwd() + "/src/assets/settings.skrillec"
    bot_prefix = ";"