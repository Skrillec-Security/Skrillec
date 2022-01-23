import os, sys, time

from src.utils.syn_parser import *
from src.config.main import *

config_file = open(Config.local_settings_path_backup, "r").read()
print(parse(config_file, "Bot", "token"))