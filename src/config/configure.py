import os, sys, time

from .main import *
from ..utils.syn_parser import *


class Configuration:
    def settings():
        return open(Config.local_settings_path_backup, "r").read()

    """
        Use Example:
        if get_token() != 0:
            print("Authorized")
        else:
            print("You are not authorized to use this")
            exit(0)
    """
    def get_token():
        return parse(Configuration.settings, "Bot", "token") ## this returns my token from 'settings.skrillec' file
        return 0