#!/usr/bin/python3

from pyfiglet import Figlet
from colorama import Fore
import pytube
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

    try:
        url = str(input(f"{Color.R}[*]{Color.G}INGRESA LA URL DEL VIDEO: {Color.OFF}"))

        banner()
    

        video = pytube.YouTube(url)
        print(f"\n{Color.R}Titulo .........: {Color.OFF}{video.title}\n")
        print(f"{Color.R}Duracion (seg)..:{Color.OFF} {video.length}\n")
        print(f"\n{Color.R}Descripcion.....:{Color.OFF} {video.description}\n\n")


        print(f'{Color.R}[*] {Color.G}Descargando video {Color.R}[*]{Color.OFF}\n')

        st = video.streams.get_highest_resolution()
        st.download('videos')# escribe la ruta donde se van a guardar los videos
        banner()
        
        print(f"{Color.R}[+] {Color.G}Descarga finalizada {Color.M}:) {Color.OFF}")

    except KeyboardInterrupt:
        banner()
        print(f'{Color.R}[!] Saliendo...\n')
        exit(1)

    except pytube.exceptions.RegexMatchError as e:
        banner()
        print(f'{Color.R} [!] link introducido no valido..{Color.OFF}')
        exit(1)

def main():
    donwload_video()

if __name__=="__main__":
    main() 