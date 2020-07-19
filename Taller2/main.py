from __future__ import unicode_literals
import time
from tkinter.messagebox import showinfo
import tkinter as tk
from conexion import conexionEjemplo
from conexion import conectar
from inputs import inputDatosRegistro
from inputs import inputNewNick
from inputs import inputEmail

#devuelve el perfil(admin o jugador) si no lo encuentra devulve None
def IniciarSesion(nick,password) :
    inicio= False
    perfil = None
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT nick,contraseña FROM administrador ")
    # recorremos el cursor en la tabla de administrador
    for administrador in cur :
        if(administrador[0]==nick):
            if(administrador[1]==password):
                print("\n Bienvenido "+nick+"\n")
                inicio=True
                perfil = "administrador"
    #si no se encuentra ningun administrador con el nick correspondiente,
    #recorremos a los jugadores       
    if(inicio==False):
        cur.execute("select nick,contraseña from jugador ")
        for jugador in cur:
            if(jugador[0]==nick):
                if(jugador[1]==password):
                    print("\n Bienvenido "+nick+"\n")
                    inicio=True
                    perfil = "jugador"
    cur.close()
    conn.close()                    
    return perfil

#Registra al usuario en la base de datos, recibe una lista con los datos a ingresar
def RegistrarUsuario(datosDeRegistro):
    data = datosDeRegistro
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        INSERT into Jugador (nick,nombres,apellidoP,apellidoM,correo,contraseña,pais)
        VALUES (%s, %s, %s, %s, %s, %s, %s);""", (data[0],data[1],data[2],data[3],data[4],data[5],data[6]) )
    cur.close()
    conn.commit()
    conn.close()

def getAvatar(nick):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("select * from avatar")
    found = False
    for avatar in cur :
        if(avatar[0]==nick):
            found = True
            atributes = [avatar[0],avatar[1],avatar[2],avatar[3],avatar[4]]
            return atributes     
    if(found==False):
        print("No se encontro al avatar")

def principal() :
    opcion = -1
    while opcion != "0" :
        print("Ingrese una opcion : ")
        opcion = input()
        if opcion == "1" : 
            print("Ingrese su nick :")
            nick = input()
            print("Ingrese su contraseña : ")
            password = input()
            perfil = IniciarSesion(nick,password)
            if perfil == None :
                print("Nick o contraseña incorrectos \n")
            elif perfil == "administrador" :
                print("Este es el menu del admin")
            else : 
                print("Este es el menu del jugador")  
        elif opcion == "2" :
            data = inputDatosRegistro()
            RegistrarUsuario(data)
        elif opcion == "0" :
            print("Adios , nos vemos pronto para mas lucha ")
        else :
            print("Ingrese una opcion valida")

def pop_up_msg(mensaje):
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text=mensaje)
    l.pack(pady=5)

    b = tk.Button(win, text="Ok", command=win.destroy)
    b.pack(pady=5)