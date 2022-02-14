import os, sys, time, requests

class ErrHandler:
    global err_msg
    global err_type
    err_types = ['API', 'DB Not Found', 'Setting file not found']
    def log_err(err_t, err_m):
        err_type = err_t
        err_msg = err_m
        make_log_format()

    def make_log_format():
        output = """Skrillec Bot Error Handler
______________________________________

        """


    def log_to_file(new_log):
        try:
            log_db = open(local_settings_path, "a")
            log_db.write(new_log)
            log_db.close()
            return 1
        except:
            return -1
        return 0