from conexion import conectar
import random
from funciones import getNivel

#En este archivo se econtraran todas las querys necesarias del programa

#devuelve los atributos del avatar asociado al nick del usuario
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

#Registra al usuario a la base de datos
def RegistrarUsuario(datosDeRegistro):
    data = datosDeRegistro
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        INSERT into Jugador (nick,nombres,apellidoP,apellidoM,correo,contraseña,pais,cantReportes,ban_S_N,ultimoLogin,peleasDisponibles)
        VALUES (%s, %s, %s, %s, %s, %s, %s,0,False,current_date,5);""", (data[0],data[1],data[2],data[3],data[4],data[5],data[6]) )
    cur.close()
    conn.commit()
    conn.close()


#Devuelve una matriz con el nick del jugador y la cantidad de reportes
def getReportados():
    reportados=[]
    con = conectar()
    cur = con.cursor()
    cur.execute('SELECT nick,cantreportes FROM jugador')
    for jugador in cur:
        if jugador[1] != None:
            reportados.append([jugador[0],jugador[1]])
    print(reportados)
    return reportados

#aumenta la cantidad de reportes de un jugador y devuelve True, si no lo encuentra devuelve False
def report(nick):
    conn = conectar()
    cur = conn.cursor()
    cur.execute('SELECT nick FROM jugador')
    found=False
    for jugador in cur :
        if(jugador[0]==nick):
            found=True
    if found==True:
        cur.execute('UPDATE jugador SET cantreportes = cantreportes+1 WHERE nick = (%s);',(nick,))
        cur.close()
        conn.commit()
        conn.close()
        return True
    else: 
        cur.close()
        conn.commit()
        conn.close()
        return False

#Comprueba si el nick ingresado esta repetido 
def nickExiste(nick):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT nick FROM administrador ")
    existe = False
    # recorremos el cursor en la tabla de administrador
    for administrador in cur :
        if(administrador[0]==nick):
            existe = True
    #si no se encuentra ningun administrador con el nick correspondiente,
    #recorremos a los jugadores       
    if(existe==False):
        cur.execute("SELECT nick FROM jugador ")
        for jugador in cur:
            if(jugador[0]==nick):
                existe = True   
    return existe

#Busca un oponente con el cual luchar
def getOponente(nick):
    print(nick + " está buscando oponente\n")
    #obtener todos los oponentes validos
    nivelPropio = getNivel(getAvatar(nick)[4])
    listaAvatares = []

    conn = conectar()
    cur = conn.cursor()
    #excluir al propio
    cur.execute("SELECT * FROM avatar WHERE nick != %s",(nick,))
    
    for avatar in cur :
        #excluir los que estan fuera del rango de nivel
        if(avatar[4] <= nivelPropio+1 or avatar[4] >= nivelPropio-1):
            listaAvatares.append([avatar[0],avatar[1],avatar[2],avatar[3]])
    cur.close()
    conn.close()

    #elegir uno al azar
    print(listaAvatares[random.randint(0,len(listaAvatares)-1)])


def iniciarSesion(nick,password) :
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

def banPlayer(nick):
    if(nickExiste(nick)):
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE jugador SET ban_S_N = True WHERE nick = (%s) ",(nick,))
        conn.commit()
        cur.close()
        conn.close()
        return True
    else: 
        cur.close()
        conn.close()
        return False
    



   