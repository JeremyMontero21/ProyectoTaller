print("Hola Mundo!!")
print("SIIUUUUU")

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
  

