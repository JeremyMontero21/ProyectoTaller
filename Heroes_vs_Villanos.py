#Proyecto Programado 3
#Jordan Lacayo y Jeremy Montero

import tkinter as tk
import random
import os

from tkinter import filedialog
from tkinter import messagebox

#Configuración de la ventana principal
base=tk.Tk()
base.title("El Gran Torneo (Jordan Lacayo y Jeremy Montero)")
base.state("zoomed")
ancho=base.winfo_screenwidth()
base.geometry(f"{ancho}x710")

#Control de acceso:
label_usuario = tk.Label(base, text="Nombre de usuario:")
label_usuario.place(anchor="center",relx=0.5,rely=0.45) #anchor=center es para colocarlo en el centro de la pantalla y a partir de allí moverlo. Esto es con el fin de que se muestre correctamente en cualquier dispositivo.

entry_usuario = tk.Entry(base, width=30)
entry_usuario.place(anchor="center",relx=0.5,rely=0.5)

label_contra = tk.Label(base, text="Contraseña:")
label_contra.place(anchor="center",relx=0.5,rely=0.55)

entry_contra = tk.Entry(base, width=30)
entry_contra.place(anchor="center",relx=0.5,rely=0.6)

#E:Ninguna.
#S:Si el usuario ingresó correctamente el nombre de usuario y contraseña, entrará a la aplicación. En caso contrario, saldrá un mensaje de error.
#R:Para poder ingresar a la aplicación, se deben ingresar correctamente ambos datos.
#Descripción: Permite validar si el nombre y la contraseña se encuentran en el archivo acceso.txt.
def acceso():
  exito=False #Valor booleano que indica si el usuario pudo ingresar o no.
  usuario=entry_usuario.get()
  contra=entry_contra.get()
  if not usuario or not contra:
    messagebox.showwarning("Campos incompletos", "Debes completar todos los campos solicitados.")
  else:
    with open("acceso.txt","r",encoding="utf-8") as acceso:
      for linea in acceso:
        _usuario_=linea.strip().split(";")[1]
        _contra_=linea.strip().split(";")[2]
        if usuario==_usuario_ and contra==_contra_:
          for elem in [label_usuario,entry_usuario,label_contra,entry_contra,btn_ingresar]:
            elem.place_forget()
          btn_crear_prsnje.place(anchor="center",relx=0.5,rely=0.25)
          btn_borrar_prsnje.place(anchor="center",relx=0.5,rely=0.35)
          btn_crear_torneo.place(anchor="center",relx=0.5,rely=0.45)
          btn_borrar_torneo.place(anchor="center",relx=0.5,rely=0.55)
          btn_jugar_torneo.place(anchor="center",relx=0.5,rely=0.65)
          btn_stats.place(anchor="center",relx=0.5,rely=0.75)
          exito=True
          break
      if not exito:
        messagebox.showerror("Error","El nombre de usuario o contraseña son incorrectos.")

#Botón de ingresar:
btn_ingresar = tk.Button(base, text="Ingresar", command=acceso)
btn_ingresar.place(anchor="center",relx=0.5,rely=0.7)

#------------------------------------------------------Menú Principal--------------------------------------------------------------------#

#E:
#S:
#R:
#Descripción:
def crear_personaje():
  return

#E:
#S:
#R:
#Descripción:
def borrar_personaje():
  return

#E:
#S:
#R:
#Descripción:
def crear_torneo():
  return

#E:
#S:
#R:
#Descripción:
def borrar_torneo():
  return

#E:
#S:
#R:
#Descripción:
def jugar_torneo():
  return

#E:
#S:
#R:
#Descripción:
def stats():
  return
  
#Botones:
btn_crear_prsnje = tk.Button(base, text="Crear personaje", command=crear_personaje)
btn_borrar_prsnje = tk.Button(base, text="Borrar personaje", command=borrar_personaje)
btn_crear_torneo = tk.Button(base, text="Crear torneo", command=crear_torneo)
btn_borrar_torneo = tk.Button(base, text="Borrar torneo", command=borrar_torneo)
btn_jugar_torneo = tk.Button(base, text="Jugar torneo", command=jugar_torneo)
btn_stats = tk.Button(base, text="Estadísticas", command=stats)
        
#-----------------------------------------------------------------------------------------------------------------------------------------

"""
Clase: Personaje.
Atributos:
  Tipo: Héroe/Villano
  Sexo: Mujer/Hombre/No determinado
  Nombre completo
  Nombre de su alter ego.
  Foto: ruta del archivo
  Velocidad
  Fuerza
  Inteligencia
  Defensa personal
  Magia
  Telepatía
  Estratega
  Volar
  Elasticidad
  Regeneración
Métodos:
"""
class personaje:
  def __init__(self,tipo,sexo,nom_comp,nom_alt_ego,foto,speed,fuerza,intelig,defensa,magia,telepat,estrateg,volar,elastic,regen):
    self.tipo=tipo
    self.sexo=sexo
    self.nombre_completo=nom_comp
    self.nombre_alter_ego=nom_alt_ego
    self.foto=foto
    self.velocidad=speed
    self.fuerza=fuerza
    self.inteligencia=intelig
    self.defensa=defensa
    self.magia=magia
    self.telepatia=telepat
    self.estratega=estrateg
    self.volar=volar
    self.elasticidad=elastic
    self.regeneracion=regen

"""
Clase: Torneo.
Atributos:
  Nombre del torneo
  Fecha
  Lugar del torneo
  Número de luchas
  Luchas: lista de objetos de tipo Lucha
  Bando Ganador
Métodos:
"""
class torneo:
  def __init__(self,nom,fecha,lugar,num_luchas,list_luchas,ganador):
    self.nombre=nom
    self.fecha=fecha
    self.lugar=lugar
    self.numero_luchas=num_luchas
    self.luchas=list_luchas
    self.bando_ganador=ganador

"""
Clase Lucha.
Atributos:
  Nombre del alter ego del primer luchador
  Nombre del alter ego del segundo luchador
  Ganador del 1er round
  Ganador del 2do round
  Ganador del 3er round
  Ganador de la lucha
Métodos:
"""
class lucha:
  def __init__(luchador1,luchador2,ganador_r1,ganador_r2,ganador_r3,ganador_lucha):
    self.alterego_luchador1=luchador1
    self.alterego_luchador2=luchador2
    self.ganador_round1=ganador_r1
    self.ganador_round2=ganador_r2
    self.ganador_round3=ganador_r3
    self.ganador_lucha=ganador_lucha

base.mainloop()
