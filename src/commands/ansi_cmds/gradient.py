import os, sys, time, subprocess, random

from .gradient import *
from ...discord_utils.embed_msg import *

async def gradient(client, args):
    if len(args) == 0 | len(args) < 3: return (await embed(client, "Error", "Invalid argument(s)\nUsage: ;fade <color1> <color2> <text>"))

    ## Get ARGUMENTs 
    color1 = args[1]
    color2 = args[2]

    text = ""

    for i in args[3:]:
        text += i + " "

    """
        Removing characters that will break the command or characters that can cause bad things to happen to the box!
    """
    text = text.replace("'", "")
    text = text.replace(";", "")
    text = text.replace("|", "")
    text = text.replace("`", "")
    text = text.replace('\\', "")
    text = text.replace(",", "")
    text = text.replace("IFS", "")
    text = text.replace('$', "")
    text = text.replace('"', "")

    ANSI_File = generate_filename()

    try:
        CMD = "echo {0} | /home/ubuntu/bot/src/commands/ansi_cmds/fade {1} {2} > {3}.txt; cat {3}.txt".format(text, color1, color2, ANSI_File)
        print(CMD)
        check_grad = subprocess.getoutput(CMD)
        print(check_grad)

        ## Move the file to web server

        check_code = subprocess.getoutput("sudo mv {0}.txt /var/www/html/ansi/".format(ANSI_File))
        print(check_code)

        return await embed(client, "ANSI Gradient Command", "https://api.skrillec.pw/ansi/{0}.txt".format(ANSI_File))
    except:
        return await embed(client, "Error", "An exception error has occurred, Try again....")

def generate_filename():
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
    num = random.randint(0, len(chars))
    last_num = 0
    file_name = ""
    for i in range(0, 10):
        if num == last_num:
            num = random.randint(0, len(chars))
        last_num = num
        file_name += chars[num]
    return file_name