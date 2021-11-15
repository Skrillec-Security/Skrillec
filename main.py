import os, sys, time, threading, discord
from src.Bot.main import *
from src.Config.main import *

bot = Skrillec()
threading.Thread(target=bot.run, args=('OTA5NTAwOTkwMTM3NDQyNDE2.YZFMzQ.MGAdb6rsyU1OOGFrOAgIYLKCi_M',)).start()
while(1):
    input_cmd = input(">>> ")
    if input_cmd == "c":
        exit(0)
    
