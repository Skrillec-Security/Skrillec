import os, sys, time

def ipv4_check(ip: str):
    try:
        if len(ip) <= len("255.255.255.255"):
            for i in range(0, 4):
                if ip.contains("."): continue
                else: return 0
            ip_args = ip.split(".")
            if ip_args[0].int() > 255: return 0
            if ip_args[1].int() > 255: return 0
            if ip_args[2].int() > 255: return 0
            if ip_args[3].int() > 255: return 0
    except:
        return 0
    return 1

def remove_all_spaces(skid):
    return skid.replace(" ", "")