import tkinter as tk
from tkinter.messagebox import showinfo

def registro():

    window = tk.Tk()
    window.title("Registro de cuenta nueva ")
    window.geometry("400x400")
    #titulo del menu
    window.configure(background = 'black')

    nickLabel = tk.Label(text="Ingrse su Nick",bg='black',fg='white')
    nickLabel.pack()
    nickEntry = tk.Entry(window)
    nickEntry.pack()

    passLabel = tk.Label(text="Ingrese su Contraseña",bg='black',fg='white')
    passLabel.pack()
    passEntry = tk.Entry(window,show ="*")
    passEntry.pack()

    pass2Label = tk.Label(text="Ingrese su Contraseña otra vez",bg='black',fg='white')
    pass2Label.pack()
    pass2Entry = tk.Entry(window,show ="*")
    pass2Entry.pack()

    nombreLabel = tk.Label(text="Ingrese su nombre",bg='black',fg='white')
    nombreLabel.pack()
    nombreEntry = tk.Entry(window)
    nombreEntry.pack()

    aPaternoLabel = tk.Label(text="Ingrese su apellido paterno",bg='black',fg='white')
    aPaternoLabel.pack()
    aPaternoEntry = tk.Entry(window)
    aPaternoEntry.pack()

    aMaternoLabel = tk.Label(text="Ingrese su apellido materno",bg='black',fg='white')
    aMaternoLabel.pack()
    aMaternoEntry = tk.Entry(window)
    aMaternoEntry.pack()

    paisLabel = tk.Label(text="Pais",bg='black',fg='white')
    paisLabel.pack()
    paisEntry = tk.Entry(window)
    paisEntry.pack()