import os, sys, time

from .custom_utils import *

def parse(syn_format: str, field, key):
    if "\n" not in str(syn_format): return 0
    lines = syn_format.split("\n")
    line_count = 0
    for i in lines:
        if i.startswith(field) and i.endswith("{") or i.startswith(field + " {"):
            found = 0
            find_c = line_count+1
            while(1):
                if "{" in lines[find_c]: return 0
                if (key + " ") in lines[find_c]:
                    split_lines = lines[find_c].replace(key + " ", "").replace("=", "")
                    if "//" in lines[find_c]:
                        split_lines = split_lines.split("/")[0]
                    if "\"" in lines[find_c]:
                        split_lines = split_lines.replace("\"", "")
                    return remove_all_spaces(split_lines)
                find_c+=1
        line_count+=1
    return ""