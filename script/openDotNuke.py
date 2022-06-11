import os
import platform
import subprocess

def openDotNuke():
    path = os.getenv('HOME') + "/.nuke"
    operatingSystem = platform.system()

    if operatingSystem == "Windows":
        subprocess.Popen("explorer {}".format(path.replace('/', '\\')))

    elif operatingSystem == "Darwin":
        subprocess.Popen(["open", path])

    else:
        subprocess.Popen(["xdg-open", path])