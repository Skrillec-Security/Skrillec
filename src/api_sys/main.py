import os, sys, time, api_sys
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED

from ..config.main import *

class API_Crud:
    def parse_dbLine(line):
        return (line.replace("('", "").replace("')", "")).split("','")

    def apis():
        return open(Config.local_api_path, "r").read()

    def add_api(api_name, api_url, api_methods, api_funnels):
        try:
            apis_db = open(Config.local_api_path, "a")
            apis_db.write("('{0}','{1}','{2}','{3}')".format(api_name, api_url, api_methods, api_funnels))
            apis_db.close()
            return 1
        except:
            return 0
        return 0

    def remove_api(api_name):
        try:
            apis_db = API_Crud.apis().split("\n")
            new_db = ""
            for api in apis_db:
                if api_name in api:
                    continue
                else:
                    new_db += api
            db = open(Config.local_api_path, "w")
            db.write(new_db)
            db.close()
            return 1
        except:
            return 0
        return 0

    def update_api(api_name, new_url, new_methods, new_funnels):
        try:
            apis_db = API_Crud.apis().split("\n")
            new_db = ""
            for api in apis_db:
                if api_name in api:
                    n = (api.replace("('", "").replace("')", "")).split("','")
                    new_info = "('"
                    if new_url != "": new_info += "{}','".format(new_url)
                    if new_methods != "": new_info += "{}','".format(new_methods)
                    if new_funnels != "": new_info += "{}')".format(new_funnels)
                    new_db += "('{0}','{1}','{2}','{3}','{4}')".format(api_name, new_url, new_methods, new_funnels)
                else:
                    new_db = api
                db = open(Config.local_api_path, "w")
                db.write(new_info)
                db.close()
            return 1
        except:
            return 0
    
    def api_count():
        return len(API_Crud.api())

    def get_api(api_name):
        try:
            apis = API_Crud.apis().split("\n")
            for api in apis:
                if api_name in apis:
                    return API_Crud.parse_dbLine(api)
            return 1
        except:
            return 0
