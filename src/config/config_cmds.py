import os, sys, time

def get_cmds():
    all_cmds = os.listdir(os.getcwd() + "/src/commands/")
    new_list = ["", ""]
    for i in all_cmds:
        new_list.append(i.replace(".py", ""))
    return new_list
