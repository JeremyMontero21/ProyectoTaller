#Proyecto Programado 3
#Jordan Lacayo y Jeremy Montero

import tkinter as tk
import random
import os

from tkinter import filedialog

#Configuración de la ventana principal
base=tk.Tk()
base.title("El Gran Torneo (Jordan Lacayo y Jeremy Montero)")
base.state("zoomed")
ancho=base.winfo_screenwidth()
base.geometry(f"{ancho}x710")

#Control de acceso:
label_usuario = tk.Label(base, text="Nombre de usuario:").place(anchor="center",relx=0.5,rely=0.45) #anchor=center es para colocarlo en el centro de la pantalla y a partir de allí moverlo. Esto es con el fin de que se muestre correctamente en cualquier dispositivo.
entry_usuario = tk.Entry(base, width=30)
entry_usuario.place(anchor="center",relx=0.5,rely=0.5)

label_contra = tk.Label(base, text="Contraseña:").place(anchor="center",relx=0.5,rely=0.55)
entry_contra = tk.Entry(base, width=30)
entry_contra.place(anchor="center",relx=0.5,rely=0.6)

#Mensaje de error en el acceso:
error_acceso = tk.Label(base, text="Error: el nombre de usuario o la contraseña son incorrectos.")

#E:Ninguna.
#S:Si el usuario ingresó correctamente el nombre de usuario y contraseña, entrará a la aplicación. En caso contrario, saldrá un mensaje de error.
#R:Para poder ingresar a la aplicación, se deben ingresar correctamente ambos datos.
#Descripción: Permite validar si el nombre y la contraseña se encuentran en el archivo acceso.txt.
def acceso():
  usuario=entry_usuario.get()
  contra=entry_contra.get()

  with open("acceso.txt","r",encoding="utf-8") as acceso:
    for linea in acceso:
      _usuario_=linea.strip().split(";")[1]
      _contra_=linea.strip().split(";")[2]
      if usuario==_usuario_ and contra==_contra_:
        for elem in [label_usuario,entry_usuario,label_contra,entry_contra]:
          elem.place_forget()
      else:
        error_acceso.place(anchor="center",relx=0.5,rely=0.7)
        base.after(3500, lambda: error_acceso.place_forget())
        
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
