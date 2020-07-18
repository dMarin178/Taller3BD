import tkinter as tk
from main import IniciarSesion
from tkinter.messagebox import showinfo


def menu():
    window = tk.Tk()
    window.title("El bruto")
    window.geometry("300x300")
    #definimos variables
    nick=tk.StringVar()
    password=tk.StringVar()
    #titulo del menu
    window.configure(background = 'black')
    titulo = tk.Label(window, text = "EL BRUTO",bg='black',fg='white')
    titulo.pack(pady=10)

    nickLabel = tk.Label(text="Nick",bg='black',fg='white')
    nickLabel.pack()
    nickEntry = tk.Entry(window,textvariable=nick)
    nickEntry.pack()

    passLabel = tk.Label(text="Contraseña",bg='black',fg='white')
    passLabel.pack()
    passEntry = tk.Entry(window,textvariable=password,show ="*")
    passEntry.pack()

    inicioSesion = tk.Button(text = "Iniciar sesion", command=lambda: login(nick,password))
    inicioSesion.pack(pady=15)

    Registrarse = tk.Button(text="Registrarse")
    Registrarse.pack(pady=20)

    window.mainloop()

def menuAdmin():
    print("este es el menu del administrador")

def menuJugador():
    print("Este es el menu del jugador")

def login(nick,password):
    sesion = IniciarSesion(nick,password)
    if(sesion != None):
        if(sesion == "administrador"):
            menuAdmin()
        else :
            menuJugador()
    else: pop_up_msg(" Nombre o contraseña incorrecto ")


def pop_up_msg(mensaje):
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text=mensaje)
    l.grid(row=0, column=0)

    b = tk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


menu()







