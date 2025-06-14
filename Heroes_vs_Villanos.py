#Proyecto Programado 3
#Jordan Lacayo y Jeremy Montero

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
