# Skrillec
 An Advanced Moderation BOT with extra cool tools/commands!

## Install Dependencies
Install Python3.8+
```
pip3 install requests
pip3 install discord
```

## Start Bot
Windows
```
Run the start_bot.bat file
```
Linux
```
python3 main.py
```

## How to add commands
- Create the file for command function in a folder designed for the related action your command does, under ``src/commands/`` 
```
Folder Tree

src/commands/
     - account_cmds/
     - admin_cmds/
     - ansi_cmds/
     - attack_cmds/
     - mod_cmds/
     - tools_cmds/
     - auto_role.py
     - help.py
     - invite.py
```
- Create a function with client argument in the file to call in the bot source
- import the file you created in ``src/bot/command_handler.py``
- add an elif in the command handler's if statement, here an example on how you would do it
```
from ..commands.folder_your_file_in.your_file_name import *

elif cmd == "command": command_function(client)
```
You're command should be successfully added! 
