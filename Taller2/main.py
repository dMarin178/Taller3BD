from __future__ import unicode_literals
import time
from conexion import conexionEjemplo
from conexion import conectar()

def menu():
    print("Bienvenido a El Bruto \n")
    print("1) Iniciar sesion")
    print("2) Registrarse")
    print("0) Salir")

def IniciarSesion(nick,password) :
    inicio= False
    perfil = None
        cur = conectar()
        cur.execute("select nick,contraseña from administrador ")
        # recorremos el cursor en la tabla de administrador
        for administrador in cur :
            if(administrador[0]==nick):
                if(administrador[1]==password):
                    #print("\n Bienvenido "+nick+"\n")
                    inicio=True
                    perfil = "administrador"
        #si no se encuentra ningun administrador con el nick correspondiente,
        #recorremos a los jugadores       
        if(inicio==False):
            cur.execute("select nick,contraseña from jugador ")
            for jugador in cur:
                if(jugador[0]==nick):
                    if(jugador[1]==password):
                        #print("\n Bienvenido "+nick+"\n")
                        inicio=True
                        perfil = "jugador"
        # Cerrar el cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return perfil

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

def menuAdmin(nick):
    print("Este es el menu del administrador \n")

def menuJugador(nick):
    print("Este es el menu del jugador \n ")

def principal() :
    opcion = -1
    while opcion != "0" :
        menu()
        print("Ingrese una opcion : ")
        opcion = input()
        if opcion == "1" : 
            print("Ingrese su nick :")
            nick = input()
            print("Ingrese su contraseña : ")
            password = input()
            sesion = IniciarSesion(nick,password)
            if sesion == None :
                print("Nick o contraseña incorrectos \n")
            elif sesion == "administrador" :
                menuAdmin(nick)
            else : 
                menuJugador(nick)    
        elif opcion == "2" :
            print("Ingrese su nick con el que iniciara sesion : ")
            nick = input()
            print("Ingrese sus nombres : ")
            nombres = input()
            print("Ingrese su apellido paterno :")
            apellidoP = input()
            print("Ingrese su apellido materno : ")
            apellidoM = input()
            correo = emailVerification()
            print("Ingrese su país : ")
            pais = input()
            print("Ingrese su constraseña : ")
            password = input()
            RegistrarUsuario(nick,nombres,apellidoP,apellidoM,correo,password,pais)
        elif opcion == "0" :
            print("Adios , nos vemos pronto para mas lucha ")
        else :
            print("Ingrese una opcion valida")
 
def getAvatar(nick):
    try:
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
            print("No se encontro al usuario")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

conexionEjemplo()

