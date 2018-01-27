#   run this on remote machine
#   make sure to `sudo apt-get install sshpass`

import sys
import os
import subprocess

data = {"user": "pi",
        "host": "192.168.1.223",
        "password": "raspberry",
        "commands": " " .join([" python git/pi-pictures/camera.py", "echo 'up yours'"])}
        # "commands": " python git/pi-pictures/camera.py"}

command = "sshpass -p {password} ssh {user}@{host} {commands}"
os.system(command.format(**data))

subprocess.call("echo 'password is `raspberry`' ", shell=True)
subprocess.call("scp pi@192.168.1.223:picture.jpg . ", shell=True)
subprocess.call("xdg-open picture.jpg ", shell=True)