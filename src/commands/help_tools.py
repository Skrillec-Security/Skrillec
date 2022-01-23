import sys, os, time

from ..discord_utils.embed_msg import *

async def help_tools(client):
    help_cmds = """```  Usage       Tools
____________________________________
  ping        Ping an IP/URL
  geoip       IP Lookup
  pscan       Port Scanner
  url         Gets IP of URL
  ip2url      Find URL to IP
  whosis      Whois Checker
  urlr        Advanced DNS Checker
  skype       Skype Resolver
  phone       Phone Lookup
  
  More tools coming soon!```"""
    await embed(client, "Tools Commands", help_cmds)