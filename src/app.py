#!/usr/bin/python3

from pyfiglet import Figlet
from pafy import pafy
from colorama import Fore
import platform
import os

# Author: kiolo45,(jakepy)

"""
COLORES DE LETRA:
BLACK = '\033[30m'
RED = '\033[31m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'BLACK = '\033[30m'
"""

class Color:
    B = Fore.BLACK
    G = Fore.GREEN
    R = Fore.RED
    M = Fore.MAGENTA
    C = Fore.CYAN
    W = Fore.WHITE
    OFF = Fore.RESET


def clear():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        exit(1)

def banner():
    # banner
    clear()
    ban = Figlet(font="alligator")
    print(ban.renderText("Pymp4"))
    print(f"{Color.R}[*]{Color.G}create By: {Color.M}Kiolo45 {Color.C}and {Color.B}Jakepy\n {Color.OFF}")


def donwload_video():
    banner()

    url = str(input(f"{Color.R}[*]{Color.G}INGRESA LA URL DEL VIDEO: {Color.OFF}"))

    video = pafy.new(url)

    streams = video.streams

    for s in streams:
        print(s)

    best = video.getbest()
    print(best.resolution, best.extension)

    os.system("mkdir ~/archivo")
    best.download(filepath=("~/archivo")) # escribe la ruta donde se van a guardar los videos
    print(f"{Color.R}[+] {Color.G}Descarga finalizada {Color.M}:) {Color.OFF}")


def main():
    donwload_video()

if __name__=="__main__":
    main() 
