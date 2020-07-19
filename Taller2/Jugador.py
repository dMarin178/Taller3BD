from conexion import conectar


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
    

#devuelve el nivel que se encuentra el jugador
def getNivel(ptosExperiencia):
    if(ptosExperiencia < 150):
        return 1
    else:
        nivel = abs((ptosExperiencia-100)//50)
        return nivel

#devuelve los puntos de experiencia necesarios para subir de nivel
def nextLvl(nivel):
    ptos=nivel*50+100
    return ptos
