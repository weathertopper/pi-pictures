#   run this on remote machine
#   make sure to `sudo apt-get install sshpass`

import sys
import os

data = {"user": "pi",
        "host": "192.168.1.223",
        "password": "raspberry",
        "commands": " python git/pi-pictures/camera.py"}

command = "sshpass -p {password} ssh {user}@{host} {commands}"
os.system(command.format(**data))