from pyfiglet import Figlet
from pafy import pafy

__autor__ = "Kiolo45"

"""
COLORES DE LETRA:
BLACK = '\033[30m'
RED = '\033[31m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'BLACK = '\033[30m'
"""

# tema de letra 
custom_fig = Figlet("graffiti")
RED = '\033[31m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
GREEN = '\033[32m'

# titulo
m = custom_fig.renderText("mp4 Descargar")
print(YELLOW+m)
print(RED+"create By: Kiolo45\n")


def main():
    url = input(BLUE+"INGRESA LA URL DEL VIDEO: ")

    video = pafy.new(url)

    streams = video.streams

    for s in streams:
        print(s)

    best = video.getbest()
    print(best.resolution, best.extension)

    best.download(filepath=("/mnt/c/Users/Usuario/Desktop/descargas/")) # escribe la ruta donde se van a guardar los videos
    print("\n")
    print(GREEN+"Descarga finalizada :)")


if __name__=="__main__":
    main() 