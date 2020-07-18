from __future__ import unicode_literals
from conexion import conectar
from conexion import conexionEjemplo
import psycopg2

def inputEmail():
    conn = conectar()
    cur = conn.cursor()
    repetido = True
    while repetido == True :
        repetido = False
        print("Ingrese email : ")
        mail = input()
        cur.execute("select correo from administrador ")
        # recorremos el cursor en la tabla de administrador
        for administrador in cur :
            if(administrador[0]==mail):
                print("Correo ingresado esta asociado a otra cuenta, intente con otro.")
                repetido = True
        #si no se encuentra ningun administrador con el nick correspondiente,
        #recorremos a los jugadores       
        if(repetido==False):
            cur.execute("select correo from jugador ")
            for jugador in cur:
                if(jugador[0]==mail):
                    print("Correo ingresado esta asociado a otra cuenta, intente con otro.")
                    repetido = True
        if repetido == False:
            cur.close()
            conn.close()
            return mail   

def inputNewNick():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("select nick from administrador ")
    repetido = True
    while(repetido==True):
        repetido = False
        print("Ingrese nick de usuario: ")
        nick = input()
        # recorremos el cursor en la tabla de administrador
        for administrador in cur :
            if(administrador[0]==nick):
                print("Nick ingresado ya esta en uso, intente con otro.")
                repetido = True
        #si no se encuentra ningun administrador con el nick correspondiente,
        #recorremos a los jugadores       
        if(repetido==False):
            cur.execute("select nick from jugador ")
            for jugador in cur:
                if(jugador[0]==nick):
                    print("Nick ingresado ya esta en uso, intente con otro.")
                    repetido = True
                if repetido == False:
                    return nick        

def inputDatosRegistro():
    datos = []
    #para evitar nicks repetidos creamos la funcion inputNewNick(): string = nick
    datos.append(inputNewNick())
    print("Ingrese sus nombres : ")
    datos.append(input())
    print("Ingrese su apellido paterno :")
    datos.append(input())
    print("Ingrese su apellido materno : ")
    datos.append(input())
    #para evitar emails ya ingresados se creo la funcion emailVerification():string = mail
    datos.append(inputEmail())
    print("Ingrese su país : ")
    datos.append(input())
    print("Ingrese su constraseña : ")
    datos.append(input())
    return datos


def IniciarSesion(nick,password) :
    inicio= False
    perfil = None
    conn = conectar()
    cur = conn.cursor()
    cur.execute("select nick,contraseña from administrador ")
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
    conn.close()                    
    return perfil