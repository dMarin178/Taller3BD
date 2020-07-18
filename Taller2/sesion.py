import tkinter as tk
from tkinter.messagebox import showinfo
from functools import partial
from main import getAvatar

def menuJugador(nick):
    window = tk.Tk()
    window.title("Perfil de "+nick)
    window.geometry("400x400")
    #titulo del menu
    window.configure(background = 'black')

    avatar= getAvatar(nick)

    titulo = tk.Label(window, text = nick ,bg='black',fg='white')
    titulo.pack(pady=10)

    nickLabel = tk.Label(text="Puntos de ataque "+str(avatar[0]),bg='black',fg='white')
    nickLabel.pack()

    passLabel = tk.Label(text="Puntos de defensa"+str(avatar[1]),bg='black',fg='white')
    passLabel.pack()

    window.mainloop()
