from __future__ import unicode_literals
import time
from tkinter.messagebox import showinfo
import tkinter as tk
from conexion import conexionEjemplo
from conexion import conectar
from inputs import inputDatosRegistro
from inputs import inputNewNick
from inputs import inputEmail
import random 


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

   