import os, sys, time


class Config:
    ## Windows paths
    local_db_path_backup = os.getcwd() + "\\src\\assets\\db\\users.skrillec"
    local_attacks_path_backup = os.getcwd() + "\\src\\assets\\logs\\attacks.log" #attack logs
    local_cmdlog_db_path_backup = os.getcwd() + "\\src\\logs\\cmds.log" # cmds logs
    local_login_path_backup = os.getcwd() + "\\src\\assets\\logs\\logins.log" #login logs
    local_admin_path_backup = os.getcwd() + "\\src\\assets\\logs\\admin_cmds.log" # admin cmds logs
    local_settings_path_backup = os.getcwd() + "\\src\\assets\\settings.skrillec"
    local_err_path = os.getcwd() + "\\src\\assets\\logs\\erros.log"
    local_blacklist_path = os.getcwd() + "\\src\\assets\\db\\blacklisted.skrillec"



    ## Linux Paths
    local_db_path = os.getcwd() + "/src/assets/db/users.skrillec" #db
    local_attacks_path = os.getcwd() + "/src/assets/logs/attacks.log" #attack logs
    local_cmdlog_db_path = os.getcwd() + "/src/logs/cmds.log" # cmds logs
    local_login_path = os.getcwd() + "/src/assets/logs/logins.log" #login logs
    local_admin_path = os.getcwd() + "/src/assets/logs/admin_cmds.log" # admin cmds logs
    local_settings_path = os.getcwd() + "/src/assets/settings.skrillec"
    local_err_path = os.getcwd() + "/src/assets/logs/erros.log"
    local_blacklist_path = os.getcwd() + "/src/assets/db/blacklisted.skrillec"
    bot_prefix = ";"