from tkinter import *
from tkinter import messagebox as Mensaje
from pytube import YouTube


root = Tk()

def descargar():
    urls = url.get()
    video = YouTube(urls)
    descarga = video.streams.get_highest_resolution()
    descarga.download('videos')


def info():
    Mensaje.showinfo('Sobre Mi', 'mi GitHub: https://github.com/JuanPerdomo00')


def ventana():
    global url 
    root.config(bd=15)
    root.title('Pymp4')

    # imagen
    img = PhotoImage(file='./logo.png')
    foto = Label(root, image=img, bd=0)
    foto.grid(row=1, column=1)

    # barras de menu
    barra_menu = Menu(root)
    root.config(menu=barra_menu)
    menu_help = Menu(barra_menu, tearoff=0)

    barra_menu.add_cascade(label='Mas info', menu=menu_help)
    menu_help.add_command(label='Informacion de el programador', command=info)

    barra_menu.add_command(label='Salir.', command=root.destroy)


    # intrucciones
    intruccion = Label(root, text='Descargas videos de youtube :D \n')
    intruccion.grid(row=0, column=1)

    # pedir la url
    url = Entry(root)
    url.grid(row=3, column=1)

    # boton
    boton = Button(root, text='Descargar', command=descargar)
    boton.grid(row=3, column=3)


    root.mainloop()



def main():
    ventana()

if __name__ == '__main__':
    main()