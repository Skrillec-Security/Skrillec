from distutils.command import config
import os, sys, time

def get_apis():
    api = open(os.getcwd() + "/src/assets/apis.skrillec", "r").split("\n")
    if len(api) == 0: return ""
    return api
