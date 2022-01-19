import os, sys, time
# Import Submodules (Commands)
from ..commands.help import *
from ..commands.clear import *

class Config:
    local_db_path = os.getcwd() + "/src/assets/users.skrillec"
    bot_prefix = ";"