import os, sys, time

from .crud import *
from ..err_handler.main import *

"""
  discord name   discord id         lvl mtime conn ongoing admin expiry
      0                 1            2   3   4   5   6     7
('0xLulz#0646','918258241576792115','0','0','0','0','0','0/0/0000')
"""
class Auth:
    def isRegistered(userid):
        check = Crud.find_user(userid) ## THIS FUNCTION IS WEIRD. I HAVE IT RETURNING AN ARRAY OR A INT (0) LOL
        print(check)
        if check != 0: return 1
        return check
        
    def isPremium(userid):
        check = Crud.find_user(userid)
        print(check)
        if check == 0: return check
        if check[2] != 0: return 1

    def isAdmin(userid):
        check = Crud.find_user(userid)
        print(check)
        if check == 0: return check
        if check[7] != 0 and check[7] <= 3: return 1

    def mtime_validation(userid, time_used):
        check = Crud.find_user(userid)
        print(check)
        if check == 0: return check
        if check[3] > time_used: return 0 ## TIME USED IS OVER THE USER's MAX TIME!

    def attack_valiation(userid, ip, p, t, m):
        ## Get user info
        check = Crud.find_user(userid)
        if check == 0: return check ## Failed to get user info
        if check == -1: return check
        