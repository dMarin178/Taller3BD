import tkinter as tk
from tkinter.messagebox import showinfo
from functools import partial
import tkinter.font as tkFont
from Jugador import getAvatar
from Jugador import report
from main import pop_up_msg
from conexion import conectar


def menuJugador(nick):
    sesionJugador = tk.Tk()
    sesionJugador.title("Perfil de "+nick)
    sesionJugador.geometry("400x400")
    #titulo del menu
    sesionJugador.configure(background = 'black')

    avatar= getAvatar(nick)

    titulo = tk.Label(sesionJugador, text = nick ,bg='black',fg='white', font= tkFont.Font(size=20))
    titulo.pack(pady=20)

    ptsAtck = tk.Label(sesionJugador ,text="Puntos de ataque : "+str(avatar[1]),bg='black',fg='white')
    ptsAtck.pack(pady=5)

    ptsDef = tk.Label(sesionJugador,text="Puntos de velocidad : "+str(avatar[2]),bg='black',fg='white')
    ptsDef.pack(pady=5)

    ptosVel = tk.Label(sesionJugador,text="Puntos de vida : "+str(avatar[3]),bg='black',fg='white')
    ptosVel.pack(pady=5)

    lvl = tk.Label(sesionJugador,text="nivel : "+ str(getNivel(avatar[4])),bg='black',fg='white')
    lvl.pack(pady=5)

    ptosExp=tk.Label(sesionJugador,text="experiencia : "+str(avatar[4])+"/"+str(nextLvl(getNivel(avatar[3]))) ,bg='black',fg='white')
    ptosExp.pack(pady=5)

    reportarJugador = tk.Button(sesionJugador ,text="Reportar jugador",command=reportPlayer)
    reportarJugador.pack(pady=10)

    luchar= tk.Button(sesionJugador,text="Luchar")
    luchar.pack(pady=10)

    cerrarSesion= tk.Button(sesionJugador,text="Cerrar sesion",command=sesionJugador.destroy)
    cerrarSesion.pack(pady=10)

    sesionJugador.mainloop()

def reportPlayer():
    reportWindow = tk.Tk()
    reportWindow.title("Reportar Jugador")
    reportWindow.geometry("280x200")
    reportWindow.configure(background = 'black')

    reportText = tk.Label(reportWindow,text = 'Ingrese el nick del jugador que desea reportar ',bg='black', fg='white')
    reportText.pack(pady=10)

    reportEntry = tk.Entry(reportWindow)
    reportEntry.pack(pady=5)

    def reportSinParametros():
        reportNick = reportEntry.get()
        if report(reportNick) == False:
            pop_up_msg("No se encontro al jugador. ")
        else: pop_up_msg("Jugador reportado ")

    reportButton = tk.Button(reportWindow, text='Reportar', command=reportSinParametros)
    reportButton.pack(pady=10)

    backButton = tk.Button(reportWindow,text="Volver", command=reportWindow.destroy)
    backButton.pack(pady=10)
    
    reportWindow.mainloop()

def menuAdmin(nick):
    sesionAdmin = tk.Tk()
    sesionAdmin.title("Administrador "+nick)
    sesionAdmin.geometry("400x400")
    #titulo del menu
    sesionAdmin.configure(background = 'black')

    avatar= getAvatar(nick)

    titulo = tk.Label(sesionAdmin, text = "Bienvenido "+nick ,bg='black',fg='white', font= tkFont.Font(size=20))
    titulo.pack(pady=20)

    ptsAtck = tk.Label(sesionAdmin ,text="Lista de jugadores : ",bg='black',fg='white')
    ptsAtck.pack(pady=5)

    ptsDef = tk.Label(sesionAdmin,text="Puntos de vida : "+str(avatar[2]),bg='black',fg='white')
    ptsDef.pack(pady=5)

    ptosVel = tk.Label(sesionAdmin,text="Puntos de velocidad : "+str(avatar[3]),bg='black',fg='white')
    ptosVel.pack(pady=5)

    lvl = tk.Label(sesionAdmin,text="nivel : "+ str(getNivel(avatar[3])),bg='black',fg='white')
    lvl.pack(pady=5)

    ptosExp=tk.Label(sesionAdmin,text="experiencia : "+str(avatar[3])+"/"+str(nextLvl(getNivel(avatar[3]))) ,bg='black',fg='white')
    ptosExp.pack(pady=5)

    reportarJugador = tk.Button(sesionAdmin ,text="Reportar jugador",command=reportPlayer)
    reportarJugador.pack(pady=10)

    luchar= tk.Button(sesionAdmin,text="Luchar")
    luchar.pack(pady=10)

    cerrarSesion= tk.Button(sesionAdmin,text="Cerrar sesion",command=sesionJugador.destroy)
    cerrarSesion.pack(pady=10)

    sesionJugador.mainloop()
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

