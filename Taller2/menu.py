import tkinter as tk
from main import IniciarSesion
from tkinter.messagebox import showinfo
from functools import partial
from sesion import menuJugador
from main import pop_up_msg
from registro import registro
from tkinter import *
from sesion import getReportados

def menu():
    window = tk.Tk()
    window.title("El bruto")
    window.geometry("300x300")
    #titulo del menu
    window.configure(background = 'black')
    titulo = tk.Label(window, text = "EL BRUTO",bg='black',fg='white')
    titulo.pack(pady=10)

    nickLabel = tk.Label(text="Nick",bg='black',fg='white')
    nickLabel.pack()
    nickEntry = tk.Entry(window)
    nickEntry.pack()

    passLabel = tk.Label(text="Contraseña",bg='black',fg='white')
    passLabel.pack()
    passEntry = tk.Entry(window,show ="*")
    passEntry.pack()

    def loginSinParametros():
        login(nickEntry.get(),passEntry.get())

    inicioSesion = tk.Button(text = "Iniciar sesion", command=loginSinParametros)
    inicioSesion.pack(pady=15)

    Registrarse = tk.Button(text="Registrarse", command=iniciarRegistro)
    Registrarse.pack(pady=20)

    window.mainloop()

def iniciarRegistro():
        print("iniciando registro")
        registro()

def login(nick,password):
    print(nick)
    print(password)
    sesion = IniciarSesion(nick,password)
    if(sesion != None):
        if(sesion == "administrador"):
            menuAdmin(nick)
        else :
            menuJugador(nick)
    else: pop_up_msg(" Nombre o contraseña incorrecto ")
    return 0

 getReportados()






