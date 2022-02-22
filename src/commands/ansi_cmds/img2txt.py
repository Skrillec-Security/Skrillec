import os, sys, time, requests, subprocess

from .gradient import *
from ...config.main import *
from ...discord_utils.embed_msg import *

async def img2txt(client, args):
    if len(args) == 0 | len(args) < 1:
        return await embed(client, "Error", "[x] Invalid argument\nUsage: {}img2txt <url>".format(config.bot_prefix))

    url = args[1]


    """
        Generate filename to save image to
        Request image URL
        Saves PNG to file
    """
    img = requests.get(url)
    filename = generate_filename() + ".png"
    asni_filename = generate_filename() + ".txt"
        ## Love being dual monitor. its the best brb a sec
    file = open(filename, "wb")
    file.write(file.content)
    file.close()

    """
        Removing characters that will break the command or characters that can cause bad things to happen to the box!
    """
    url = url.replace("'", "")
    url = url.replace(";", "")
    url = url.replace("|", "")
    url = url.replace("`", "")
    url = url.replace('\\', "")
    url = url.replace(",", "")
    url = url.replace("IFS", "")
    url = url.replace('$', "")
    url = url.replace('"', "")

    subprocess.getoutput("img2txt {0} > {1}".format(filename, asni_filename))

    """
        Now lets move our ANSI image file to the web server 
    """
    subprocess.getoutput("sudo mv {0} /var/www/html/ansi/".format(asni_filename))


    return (await embed(client, "IMG2TXT", "Image converted. ANSI Link: https://api.skrillec.pw/ansi/{0}".format(asni_filename)))