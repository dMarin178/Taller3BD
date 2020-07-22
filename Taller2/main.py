from __future__ import unicode_literals
import time
from tkinter.messagebox import showinfo
import tkinter as tk
from conexion import conexionEjemplo
from conexion import conectar
from inputs import inputDatosRegistro
from inputs import inputNewNick
from inputs import inputEmail
<<<<<<< HEAD
import random 

=======
import random
from datetime import date
>>>>>>> c2ec6cf655c296ebbe9da817d0c439158a6db595

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

#Genera el avatar de un jugador dado su nick
def generarAvatar(nick):
    listaDatos = []

    ataque = random.randint(1,3)
    vida = random.randint(10,20)
    velocidad = random.randint(1,10)

    listaDatos.append(nick)
    listaDatos.append(ataque)
    listaDatos.append(velocidad)
    listaDatos.append(vida)
    listaDatos.append(0)

    conn = conectar()
    cur =conn.cursor()
    cur.execute("""
        INSERT INTO avatar (nick, ataque, velocidad, vida,ptosexp)
        VALUES (%s,%s,%s,%s,%s);""",(listaDatos[0],listaDatos[1],listaDatos[2],listaDatos[3],listaDatos[4]) )
    cur.close()
    conn.commit()
    conn.close()

    print("creado el avatar " + nick + "\n")

#Registra al usuario en la base de datos, recibe una lista con los datos a ingresar
def RegistrarUsuario(datosDeRegistro):

    data = datosDeRegistro
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        INSERT into Jugador (nick,nombres,apellidoP,apellidoM,correo,contraseña,pais,cantreportes, ban_s_n,ultimoLogin,peleasDisponibles)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (data[0],data[1],data[2],data[3],data[4],data[5],data[6],0,False,date.today(),5) )
    cur.close()
    conn.commit()
    conn.close()

<<<<<<< HEAD
def generarAvatar(nick):
    listaDatos = []
=======
    print("creado el jugador " + data[0] + "\n")
    generarAvatar(data[0])

def getAvatar(nick):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("select * from avatar ")
    found = False
    for avatar in cur :
        if(avatar[0]==nick):
            found = True
            atributes = [avatar[0],avatar[1],avatar[2],avatar[3],avatar[4]]
            return atributes     
    if(found==False):
        print("No se encontro al avatar")
>>>>>>> c2ec6cf655c296ebbe9da817d0c439158a6db595

    ataque = random.randint(1,3)
    vida = random.randint(10,20)
    velocidad = random.randint(1,10)

    listaDatos.append(nick)
    listaDatos.append(ataque)
    listaDatos.append(velocidad)
    listaDatos.append(vida)
    listaDatos.append(0)

    conn = conectar()
    cur =conn.cursor()
    cur.execute("""
        INSERT INTO avatar (nick, ataque, velocidad, vida,ptosexp)
        VALUES (%s,%s,%s,%s,%s);""",(listaDatos[0],listaDatos[1],listaDatos[2],listaDatos[3],listaDatos[4]) )
    cur.close()
    conn.commit()
    conn.close()

<<<<<<< HEAD
   
=======
    b = tk.Button(win, text="Ok", command=win.destroy)
    b.pack(pady=5)
>>>>>>> c2ec6cf655c296ebbe9da817d0c439158a6db595
