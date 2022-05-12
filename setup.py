#!/usr/bin/python3

import platform
import os
import time


print("*"*49)
print("[*] Instalador de dependencias by: jakepy [*]")
print("*"*49)

try:
    import colorama
    import pyfiglet
    import pytube
    print("[*] Ya tiene todo instalado")
    exit()

except ImportError:
    print("[!] No tiene modulos instalados")
    time.sleep(1.5)
    print("[*] Descargando modulos faltantes")
    time.sleep(1.2)
    os.system("pip3 install -r requirements.txt")
    time.sleep(1.5)
    print("[*] Instalado...")
