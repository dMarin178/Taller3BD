from __future__ import unicode_literals
import psycopg2
from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as print
from prompt_toolkit.shortcuts import message_dialog

def menu():
    print("Bienvenido a El Bruto \n")
    print("1) Iniciar sesion")
    print("2) Registrarse")
    print("0) Salir")

def IniciarSesion(nick,password) :
    inicio= False
    perfil = None
    try:
        # Conectarse a la base de datos
        conn = psycopg2.connect(host="localhost", database="taller2", user="postgres",password="postgres")
        # Abrir un cursor para realizar operaciones sobre la base de datos
        cur = conn.cursor()
        # Ejecutamos la consulta para obetener los datos de la tabla Administrador
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

def RegistrarUsuario(nick,nombres,apellidoP,apellidoM,correo,password,pais):
    inicio=False;
    try:
        # Conectarse a la base de datos
        conn = psycopg2.connect(host="localhost", database="taller2", user="postgres",password="postgres")
        # Abrir un cursor para realizar operaciones sobre la base de datos
        cur = conn.cursor()
        # Ejecutamos la consulta para obetener los datos de la tabla Jugador
        cur.execute("""
            INSERT into Jugador (nick,nombres,apellidoP,apellidoM,correo,contraseña,pais)
            VALUES (%s, %s, %s, %s, %s, %s, %s);""", (nick,nombres,apellidoP,apellidoM,correo,password,pais) )
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()

def menuAdmin(nick):
    print("Este es el menu del administrador \n")

def menuJugador(nick):
    print("Este es el menu del jugador \n ")

def emailVerification():
    isEmail = False
    while(isEmail == False):
        print("Ingrese su correo :")
        correo = input()
        chars = list(correo)
        for i in chars:
            if(i)== "@":
                isEmail = True
        if isEmail == False :
            print("Debe ingresar un correo ej: example@gmail.com ")        
    return correo        
        
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

message_dialog(
    title='Example dialog window',
    text='Do you want to continue?\nPress ENTER to quit.').run()