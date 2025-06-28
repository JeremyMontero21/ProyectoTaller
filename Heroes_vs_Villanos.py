import tkinter as tk
from tkinter import messagebox

import random
from datetime import date

# ----------- COLORES Y ESTILO ----------- #
COLOR_FONDO = "#161A30"
COLOR_ACENTO = "#FFB400"
COLOR_TEXTO = "#F2EFEA"
COLOR_BOTON = "#FFB400"
COLOR_BOTON_HOVER = "#FFD700"
COLOR_BOTON_SALIR = "#B22222"

FONT_TITULO = ("Impact", 48, "bold")
FONT_LABEL = ("Arial Rounded MT Bold", 16)
FONT_ENTRY = ("Arial Rounded MT Bold", 15)
FONT_BOTON = ("Arial Rounded MT Bold", 15, "bold")
FONT_BOTON_SALIR = ("Arial Rounded MT Bold", 14, "bold")

# ----------- VENTANA PRINCIPAL ----------- #
base = tk.Tk()
base.title("EL GRAN TORNEO")
base.state("zoomed")
ancho = base.winfo_screenwidth()
base.geometry(f"{ancho}x710")
base.config(bg=COLOR_FONDO)
base.resizable(False, False)

# ----------- UTILIDADES VISUALES ----------- #
def boton_hover(e):
    e.widget.config(bg=COLOR_BOTON_HOVER, fg="#333")

def boton_leave(e):
    e.widget.config(bg=COLOR_BOTON, fg="#161A30")

def boton_salir_hover(e):
    e.widget.config(bg="#FF6F6F", fg="#fff")

def boton_salir_leave(e):
    e.widget.config(bg=COLOR_BOTON_SALIR, fg="#fff")

# ----------- FRAMES DE SECCIONES ----------- #
frame_login = tk.Frame(base, bg=COLOR_FONDO)
frame_menu = tk.Frame(base, bg=COLOR_FONDO)
frame_crearPers = tk.Frame(base, bg=COLOR_FONDO)
frame_borrarPers = tk.Frame(base, bg=COLOR_FONDO)
frame_crearTorneo = tk.Frame(base, bg=COLOR_FONDO)
frame_crearLuchasTorneo = tk.Frame(base, bg=COLOR_FONDO)
frame_borrarTorneo = tk.Frame(base, bg=COLOR_FONDO)
frame_jugar = tk.Frame(base, bg=COLOR_FONDO)
frame_stats = tk.Frame(base, bg=COLOR_FONDO)

# ----------- FUNCIONES DE PANTALLAS ----------- #
def ocultar_todos():
    for f in [frame_login, frame_menu, frame_crearPers, frame_borrarPers,
    frame_crearTorneo, frame_crearLuchasTorneo, frame_borrarTorneo, frame_jugar, frame_stats]:
        f.place_forget()

def mostrar_login():
    ocultar_todos()
    frame_login.place(relwidth=1, relheight=1)

def mostrar_menu():
    ocultar_todos()
    frame_menu.place(relwidth=1, relheight=1)

def mostrar_crearPers():
    ocultar_todos()
    frame_crearPers.place(relwidth=1, relheight=1)
    crear_formulario_personaje()

def mostrar_borrarPers():
    ocultar_todos()
    frame_borrarPers.place(relwidth=1, relheight=1)
    crear_formulario_borrar_personaje()

def mostrar_crearTorneo():
    ocultar_todos()
    frame_crearTorneo.place(relwidth=1, relheight=1)
    crear_torneo()

def mostrar_borrarTorneo():
    ocultar_todos()
    frame_borrarTorneo.place(relwidth=1, relheight=1)

def mostrar_juego():
    ocultar_todos()
    frame_jugar.place(relwidth=1, relheight=1)

def mostrar_stats():
    ocultar_todos()
    frame_stats.place(relwidth=1, relheight=1)

# ----------- LOGIN ----------- #
titulo_login = tk.Label(
    frame_login,
    text="EL GRAN TORNEO",
    bg=COLOR_FONDO,
    fg=COLOR_ACENTO,
    font=FONT_TITULO
)
titulo_login.place(relx=0.5, rely=0.18, anchor="center")

label_usuario = tk.Label(frame_login, text="Nombre de usuario:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL)
label_usuario.place(relx=0.5, rely=0.33, anchor="center")
entry_usuario = tk.Entry(frame_login, width=28, font=FONT_ENTRY, bg="#fff", fg="#333", bd=2, relief="groove")
entry_usuario.place(relx=0.5, rely=0.38, anchor="center")

label_contra = tk.Label(frame_login, text="Contraseña:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL)
label_contra.place(relx=0.5, rely=0.45, anchor="center")
entry_contra = tk.Entry(frame_login, width=28, show="*", font=FONT_ENTRY, bg="#fff", fg="#333", bd=2, relief="groove")
entry_contra.place(relx=0.5, rely=0.50, anchor="center")

def acceso():
    usuario = entry_usuario.get()
    contra = entry_contra.get()
    exito = False
    if not usuario or not contra:
        messagebox.showwarning("Campos incompletos", "Debes completar todos los campos solicitados.")
    else:
        with open("acceso.txt", "r", encoding="utf-8") as acceso:
            for linea in acceso:
                partes = linea.strip().split(";")
                if len(partes) >= 3:
                    _usuario_ = partes[1]
                    _contra_ = partes[2]
                    if usuario == _usuario_ and contra == _contra_:
                        exito = True
                        break
        if exito:
            mostrar_menu()
        else:
            messagebox.showerror("Error", "El nombre de usuario o contraseña son incorrectos.")

btn_ingresar = tk.Button(frame_login, text="Ingresar", command=acceso, font=FONT_BOTON,
width=15, bg=COLOR_BOTON, fg=COLOR_FONDO, bd=0, relief="flat", cursor="hand2",
activebackground=COLOR_BOTON_HOVER, activeforeground="#222549")
btn_ingresar.place(relx=0.5, rely=0.60, anchor="center")
btn_ingresar.bind("<Enter>", boton_hover)
btn_ingresar.bind("<Leave>", boton_leave)

# ----------- FORMULARIO CREAR PERSONAJE EN frame_crearPers ----------- #
class Personaje:
    def __init__(self, tipo, sexo, nombre_completo, alter_ego,
                 velocidad, fuerza, inteligencia, defensa_personal, magia,
                 telepatia, estratega, volar, elasticidad, regeneracion):
        self.tipo = tipo
        self.sexo = sexo
        self.nombre_completo = nombre_completo
        self.alter_ego = alter_ego
        self.velocidad = velocidad
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa_personal = defensa_personal
        self.magia = magia
        self.telepatia = telepatia
        self.estratega = estratega
        self.volar = volar
        self.elasticidad = elasticidad
        self.regeneracion = regeneracion

    def to_line(self):
        return f"{self.tipo};{self.sexo};{self.nombre_completo};{self.alter_ego};{self.velocidad};{self.fuerza};{self.inteligencia};{self.defensa_personal};{self.magia};{self.telepatia};{self.estratega};{self.volar};{self.elasticidad};{self.regeneracion}\n"

def existe_alter_ego(alter_ego, archivo="luchadores.txt"):
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(";")
            if len(partes) > 3 and partes[3].lower() == alter_ego.lower():
                return True
    return False

def guardar_personaje(personaje, archivo="luchadores.txt"):
    if existe_alter_ego(personaje.alter_ego, archivo):
        messagebox.showerror("Error", f"Ya existe un personaje con el alter ego '{personaje.alter_ego}'")
        return False
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(personaje.to_line())
    messagebox.showinfo("Éxito", "¡Personaje creado y guardado!")
    return True

def crear_formulario_personaje():
    # Limpia el frame por si acaso
    for widget in frame_crearPers.winfo_children():
        widget.destroy()

    tk.Label(frame_crearPers, text="Crear Personaje", font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_ACENTO).place(relx=0.5, rely=0.05, anchor="center")

    # --- Campos básicos ---
    tk.Label(frame_crearPers, text="Tipo:", font=FONT_LABEL, bg=COLOR_FONDO, fg=COLOR_TEXTO).place(x=90, y=110)
    tipo_var = tk.StringVar(value="Héroe")
    tk.OptionMenu(frame_crearPers, tipo_var, "Héroe", "Villano").place(x=210, y=110)

    tk.Label(frame_crearPers, text="Sexo:", font=FONT_LABEL, bg=COLOR_FONDO, fg=COLOR_TEXTO).place(x=90, y=155)
    sexo_var = tk.StringVar(value="No determinado")
    tk.OptionMenu(frame_crearPers, sexo_var, "Mujer", "Hombre", "No determinado").place(x=210, y=155)

    tk.Label(frame_crearPers, text="Nombre completo:", font=FONT_LABEL, bg=COLOR_FONDO, fg=COLOR_TEXTO).place(x=90, y=200)
    entry_nombre = tk.Entry(frame_crearPers, width=30, font=FONT_ENTRY)
    entry_nombre.place(x=260, y=202)

    tk.Label(frame_crearPers, text="Alter ego:", font=FONT_LABEL, bg=COLOR_FONDO, fg=COLOR_TEXTO).place(x=90, y=245)
    entry_alter = tk.Entry(frame_crearPers, width=30, font=FONT_ENTRY)
    entry_alter.place(x=260, y=247)

    # --- Características super ---
    labels_caracts = [
        "Velocidad", "Fuerza", "Inteligencia", "Defensa personal",
        "Magia", "Telepatía", "Estratega", "Volar", "Elasticidad", "Regeneración"
    ]
    entries_caracts = []
    for idx, nombre in enumerate(labels_caracts):
        y = 300 + idx*38
        tk.Label(frame_crearPers, text=nombre + ":", font=FONT_LABEL, bg=COLOR_FONDO, fg=COLOR_TEXTO).place(x=90, y=y)
        entry = tk.Entry(frame_crearPers, width=7, font=FONT_ENTRY)
        entry.place(x=260, y=y+2)
        entries_caracts.append(entry)

    def guardar():
        tipo = tipo_var.get()
        sexo = sexo_var.get()
        nombre_completo = entry_nombre.get().strip()
        alter_ego = entry_alter.get().strip()
        caracts = []
        for entry in entries_caracts:
            val = entry.get().strip()
            if not val.isdigit():
                messagebox.showwarning("Datos inválidos", "Todas las características deben ser números enteros.")
                return
            caracts.append(int(val))
        if not nombre_completo or not alter_ego:
            messagebox.showwarning("Campos incompletos", "El nombre completo y el nombre de alter ego no pueden estar vacíos.")
            return
        if sum(caracts) != 100:
            messagebox.showerror("Error", f"La suma de las características debe ser exactamente 100. Actualmente suma: {sum(caracts)}")
            return
        personaje = Personaje(tipo, sexo, nombre_completo, alter_ego, *caracts)
        if guardar_personaje(personaje):
            crear_formulario_personaje()  # Limpia el formulario si se guarda exitosamente

    btn_guardar = tk.Button(frame_crearPers, text="Guardar", width=15, command=guardar, bg=COLOR_BOTON, font=FONT_BOTON)
    btn_guardar.place(relx=0.5, y=690, anchor="center")

    # Botón Volver al menú
    btn_volver = tk.Button(frame_crearPers, text="Volver al menú", font=FONT_BOTON_SALIR, width=18,
        bg=COLOR_BOTON_SALIR, fg="#fff", bd=0, relief="flat", cursor="hand2", command=mostrar_menu,
        activebackground="#FF6F6F", activeforeground="#fff")
    btn_volver.place(relx=0.02, rely=0.95, anchor="sw")
    btn_volver.bind("<Enter>", boton_salir_hover)
    btn_volver.bind("<Leave>", boton_salir_leave)

# ----------- FORMULARIO BORRAR PERSONAJE EN frame_borrarPers ----------- #
def borrar_personaje_por_alter_ego(alter_ego, archivo="luchadores.txt"):
    encontrado = False
    nuevas_lineas = []
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(";")
            if len(partes) > 3 and partes[3].lower() == alter_ego.lower():
                encontrado = True
                continue  # No copiar esta línea (es la que se borra)
            nuevas_lineas.append(linea)
    if not encontrado:
        messagebox.showerror("Error", f"No existe un personaje con el alter ego '{alter_ego}'")
        return False
    with open(archivo, "w", encoding="utf-8") as f:
        for linea in nuevas_lineas:
            f.write(linea)
    messagebox.showinfo("Éxito", f"¡Personaje '{alter_ego}' borrado correctamente!")
    return True

def crear_formulario_borrar_personaje():
    # Limpia el frame por si acaso
    for widget in frame_borrarPers.winfo_children():
        widget.destroy()

    tk.Label(frame_borrarPers, text="Borrar Personaje", font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_ACENTO).place(relx=0.5, rely=0.18, anchor="center")

    tk.Label(frame_borrarPers, text="Nombre de alter ego a borrar:", font=FONT_LABEL, bg=COLOR_FONDO, fg=COLOR_TEXTO).place(relx=0.5, rely=0.34, anchor="center")
    entry_borrar = tk.Entry(frame_borrarPers, width=28, font=FONT_ENTRY, bg="#fff", fg="#333", bd=2, relief="groove")
    entry_borrar.place(relx=0.5, rely=0.39, anchor="center")

    def borrar():
        alter_ego = entry_borrar.get().strip()
        if not alter_ego:
            messagebox.showwarning("Sin datos", "Debes ingresar el nombre de alter ego a borrar.")
            return
        if borrar_personaje_por_alter_ego(alter_ego):
            entry_borrar.delete(0, tk.END)

    btn_borrar = tk.Button(frame_borrarPers, text="Borrar", width=15, command=borrar, bg=COLOR_BOTON, font=FONT_BOTON)
    btn_borrar.place(relx=0.5, rely=0.52, anchor="center")

    # Botón Volver al menú
    btn_volver = tk.Button(frame_borrarPers, text="Volver al menú", font=FONT_BOTON_SALIR, width=18,
        bg=COLOR_BOTON_SALIR, fg="#fff", bd=0, relief="flat", cursor="hand2", command=mostrar_menu,
        activebackground="#FF6F6F", activeforeground="#fff")
    btn_volver.place(relx=0.02, rely=0.95, anchor="sw")
    btn_volver.bind("<Enter>", boton_salir_hover)
    btn_volver.bind("<Leave>", boton_salir_leave)

#---------FUNCIONES AUXILIARES ÚTILES--------------#
#E: Ninguna.
#S: Lista de los nombres "alter ego" en el archivo luchadores,txt.
#R: Ninguna.
#Descripción: Obtener todos los "alter egos" de luchadores.txt.
def obtener_alter_egos():
    alter_egos = []
    with open("luchadores.txt", "r", encoding="utf-8") as luchadores:
        for linea in luchadores:
            partes = linea.strip().split(";")
            alter_ego = partes[3].strip()
            alter_egos.append(alter_ego)
    return alter_egos

#E: Ninguna.
#S: Número de luchadores guardados.
#R: Ninguno.
#Descripción: Retorna un número que representa la cantidad de personajes guardados en el archivo luchadores.txt.
def obtener_num_luchadores():
    num=0
    with open("luchadores.txt", "r", encoding="utf-8") as luchadores:
        for linea in luchadores:
            num=num+1
    return num

#E: Una lista.
#S: Valor booleano que indica si todos los elementos de una lista son diferentes.
#R: Ninguno.
#Descripción: Verificar que no existan elementos iguales en la lista.
def todos_diferentes(lista):
    vistos = []
    for elem in lista:
        if elem in vistos:
            return False
        vistos.append(elem)
    return True

#E: Dos listas.
#S: Valor booleano que indica si las dos listas no tienen ningún elemento en común.
#R: Ninguno.
#Descripción: Verificar que ambas listas sean diferentes entre sí.
def listas_no_en_comun(lista1, lista2):
    for elem in lista1:
        if elem in lista2:
            return False
    return True

# ----------- FORMULARIO CREAR TORNEO EN frame_crearTorneo ----------- #
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
    def __init__(self,nombre,fecha,lugar,num_luchas,lista_luchas):
        self.nombre=nombre
        self.fecha=fecha
        self.lugar=lugar
        self.numero_luchas=num_luchas
        self.luchas=lista_luchas
        self.bando_ganador=None

#-----Campos básicos------#
tk.Label(frame_crearTorneo, text="Nombre:", font=FONT_LABEL, bg=COLOR_FONDO, fg=COLOR_TEXTO).place(relx=0.5, rely=0.2, anchor="center")
entry_nombre = tk.Entry(frame_crearTorneo, width=30, font=FONT_ENTRY)
entry_nombre.place(relx=0.5, rely=0.24, anchor="center")

tk.Label(frame_crearTorneo, text="Lugar:", font=FONT_LABEL, bg=COLOR_FONDO, fg=COLOR_TEXTO).place(relx=0.5, rely=0.35, anchor="center")
entry_lugar = tk.Entry(frame_crearTorneo, width=30, font=FONT_ENTRY)
entry_lugar.place(relx=0.5, rely=0.39, anchor="center")

tk.Label(frame_crearTorneo, text="Cantidad de luchas:", font=FONT_LABEL, bg=COLOR_FONDO, fg=COLOR_TEXTO).place(relx=0.5, rely=0.5, anchor="center")
cant_luchas_var = tk.StringVar(value="1")
opcion_cant_luchas = tk.OptionMenu(frame_crearTorneo, cant_luchas_var, "1", "2", "3", "4", "5")
opcion_cant_luchas.config(width=53)
opcion_cant_luchas.place(relx=0.5, rely=0.54, anchor="center")

def crear_torneo():
    for entry in [entry_nombre,entry_lugar]: #Limpiar los entrys
        entry.delete(0, "end")
            
    tk.Label(frame_crearTorneo, text="Crear Torneo", font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_ACENTO).place(relx=0.5, rely=0.05, anchor="center")

    btn_manual = tk.Button(frame_crearTorneo, text="Manual", width=20,
                           command=lambda: crear_luchas_torneo("manual",entry_nombre.get(),entry_lugar.get(),int(cant_luchas_var.get())),
                           bg=COLOR_BOTON, font=FONT_BOTON)
    btn_persona = tk.Button(frame_crearTorneo, text="Persona VS Programa", width=20,
                            command=lambda: crear_luchas_torneo("persona",entry_nombre.get(),entry_lugar.get(),int(cant_luchas_var.get())),
                            bg=COLOR_BOTON, font=FONT_BOTON)
    btn_programas = tk.Button(frame_crearTorneo, text="Programa VS Programa", width=20,
                              command=lambda: crear_luchas_torneo("programa",entry_nombre.get(),entry_lugar.get(),int(cant_luchas_var.get())),
                              bg=COLOR_BOTON, font=FONT_BOTON)

    y=0.65
    for boton in [btn_manual, btn_persona, btn_programas]:
        boton.place(relx=0.5, rely=y, anchor="center")
        y=y+0.08

def crear_luchas_torneo(modo,nombre,lugar,cantidad):
    num = obtener_num_luchadores()
    
    if not nombre or not lugar:
        messagebox.showwarning("Campos incompletos", "Debes completar todos los campos solicitados.")
    elif num<cantidad*2:
        messagebox.showerror(f"Error: Solo hay {num} luchadores", f"No hay suficientes luchadores para {cantidad} luchas.")
    elif ";" in nombre or ";" in lugar:
        messagebox.showerror("Error", "El nombre y el lugar no pueden contener punto y coma (;).") #Para que no haya un error al leer el archivo torneos_creados.txt.
    elif modo=="programa":
        luchas_programas(cantidad)
    else:
        ocultar_todos()
        frame_crearLuchasTorneo.place(relwidth=1, relheight=1)

        for widget in frame_crearLuchasTorneo.winfo_children(): #Limpiar el frame
            widget.destroy()

        #Botón Atrás
        btn_atras = tk.Button(frame_crearLuchasTorneo, text="Atrás", font=FONT_BOTON_SALIR, width=18,
            bg=COLOR_BOTON_SALIR, fg="#fff", bd=0, relief="flat", cursor="hand2", command=mostrar_crearTorneo,
            activebackground="#FF6F6F", activeforeground="#fff")
        btn_atras.place(relx=0.02, rely=0.95, anchor="sw")
        btn_atras.bind("<Enter>", boton_salir_hover)
        btn_atras.bind("<Leave>", boton_salir_leave)
        
        if modo=="manual":
            luchas_manual(cantidad)
        elif modo=="persona":
            luchas_persona_vs_programa(cantidad)
        

def luchas_manual(num):
    entradas_bando1=[]
    entradas_bando2=[]
    alter_egos = obtener_alter_egos()
    subframe_luchas = tk.Frame(frame_crearLuchasTorneo, bg=COLOR_FONDO, width=400, height=300)
    subframe_luchas.place(relx=0.5, rely=0.5, anchor="center")
    
    tk.Label(subframe_luchas, text="Bando 1", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL).grid(row=0, column=0, padx=20, pady=10)
    tk.Label(subframe_luchas, text="Bando 2", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL).grid(row=0, column=1, padx=20, pady=10)

    for i in range(num):
        var1 = tk.StringVar(value=alter_egos[0])
        opc1 = tk.OptionMenu(subframe_luchas, var1, *alter_egos)
        opc1.grid(row=i+1, column=0, padx=10, pady=5)
        opc1.config(width=53)
        entradas_bando1.append(var1)

        var2 = tk.StringVar(value=alter_egos[1])
        opc2 = tk.OptionMenu(subframe_luchas, var2, *alter_egos)
        opc2.grid(row=i+1, column=1, padx=10, pady=5)
        opc2.config(width=53)
        entradas_bando2.append(var2)

    btn_guardar = tk.Button(frame_crearLuchasTorneo, text="Guardar", width=15,
                            command=lambda: guardar_torneo([var.get() for var in entradas_bando1],[var.get() for var in entradas_bando2]),
                            bg=COLOR_BOTON, font=FONT_BOTON)
    btn_guardar.place(relx=0.5, rely=0.8, anchor="center")


def luchas_persona_vs_programa(num):
    persona_bando=[]
    alter_egos = obtener_alter_egos()
    subframe_luchas = tk.Frame(frame_crearLuchasTorneo, bg=COLOR_FONDO, width=400, height=400)
    subframe_luchas.place(relx=0.5, rely=0.5, anchor="center")
    
    tk.Label(subframe_luchas, text="Bando 1", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL).grid(row=0, column=0, padx=20, pady=10)

    for i in range(num):
        var1 = tk.StringVar(value=alter_egos[0])
        opc1 = tk.OptionMenu(subframe_luchas, var1, *alter_egos)
        opc1.grid(row=i+1, column=0, padx=10, pady=5)
        opc1.config(width=53)
        persona_bando.append(var1)

    btn_guardar = tk.Button(frame_crearLuchasTorneo, text="Guardar", width=15,
                            command=lambda: programa_bando([var.get() for var in persona_bando],[]),
                            bg=COLOR_BOTON, font=FONT_BOTON)
    btn_guardar.place(relx=0.5, rely=0.8, anchor="center")


def programa_bando(luchadores_bando1,luchadores_bando2):
    alter_egos = obtener_alter_egos()
    num=len(luchadores_bando1)
    
    for luchador in alter_egos: #Para que el bando del programa no tenga ningún personaje del bando de la persona (para que no haya repetidos).
        if luchador not in luchadores_bando1:
            luchadores_bando2.append(luchador)
            
    luchadores_bando2 = random.sample(luchadores_bando2, num)
    guardar_torneo(luchadores_bando1,luchadores_bando2)


def luchas_programas(num):
    alter_egos = obtener_alter_egos()
    luchadores_bando1 = random.sample(alter_egos, num)
    disponibles = []
        
    for luchador in alter_egos: #Para que el bando 2 del programa no tenga ningún personaje del bando 1 (para que no haya repetidos).
        if luchador not in luchadores_bando1:
            disponibles.append(luchador)

    luchadores_bando2 = random.sample(disponibles, num)
    guardar_torneo(luchadores_bando1,luchadores_bando2)


def guardar_torneo(luchadores_bando1,luchadores_bando2):
    if todos_diferentes(luchadores_bando1) and todos_diferentes(luchadores_bando2):
        if listas_no_en_comun(luchadores_bando1,luchadores_bando2):
            nombre = entry_nombre.get()
            fecha = date.today().strftime("%d/%m/%Y")
            lugar = entry_lugar.get()
            cantidad = cant_luchas_var.get()
            with open("torneos_creados.txt", "a", encoding="utf-8") as torneos:
                torneos.write(f"{nombre};{fecha};{lugar};{cantidad};{luchadores_bando1};{luchadores_bando2}\n")
            messagebox.showinfo("Éxito", f"¡Torneo {nombre} creado exitosamente!")
        else:
            messagebox.showerror("Error", "Ambos bandos no pueden tener un mismo luchador.")
    else:
        messagebox.showerror("Error", "Todos los luchadores de un bando deben ser diferentes.")
        

# ----------- MENÚ PRINCIPAL ----------- #
titulo_menu = tk.Label(
    frame_menu,
    text="EL GRAN TORNEO",
    bg=COLOR_FONDO,
    fg=COLOR_ACENTO,
    font=FONT_TITULO
)
titulo_menu.place(relx=0.5, rely=0.13, anchor="center")

botones_menu = [
    ("Crear personaje", mostrar_crearPers),
    ("Borrar personaje", mostrar_borrarPers),
    ("Crear torneo", mostrar_crearTorneo),
    ("Borrar torneo", mostrar_borrarTorneo),
    ("Jugar torneo", mostrar_juego),
    ("Estadísticas", mostrar_stats)
]

for idx, (txt, cmd) in enumerate(botones_menu):
    btn = tk.Button(frame_menu, text=txt, width=25, font=FONT_BOTON, bg=COLOR_BOTON, fg=COLOR_FONDO,
    bd=0, relief="flat", cursor="hand2", command=cmd,
    activebackground=COLOR_BOTON_HOVER, activeforeground="#222549")
    btn.place(relx=0.5, rely=0.23 + idx * 0.10, anchor="center")
    btn.bind("<Enter>", boton_hover)
    btn.bind("<Leave>", boton_leave)

btn_salir = tk.Button(frame_menu, text="Cerrar sesión", width=25, font=FONT_BOTON_SALIR,
bg=COLOR_BOTON_SALIR, fg="#fff", bd=0, relief="flat", cursor="hand2",
command=mostrar_login, activebackground="#FF6F6F", activeforeground="#fff")
btn_salir.place(relx=0.5, rely=0.83, anchor="center")
btn_salir.bind("<Enter>", boton_salir_hover)
btn_salir.bind("<Leave>", boton_salir_leave)

# ----------- BOTONES DE VOLVER PARA OTROS FRAMES ----------- #
for frame, funcion in [
    (frame_crearTorneo, mostrar_menu),
    (frame_borrarTorneo, mostrar_menu),
    (frame_jugar, mostrar_menu),
    (frame_stats, mostrar_menu)
]:
    btn_volver = tk.Button(frame, text="Volver al menú", font=FONT_BOTON_SALIR, width=18,
        bg=COLOR_BOTON_SALIR, fg="#fff", bd=0, relief="flat", cursor="hand2", command=funcion,
        activebackground="#FF6F6F", activeforeground="#fff")
    btn_volver.place(relx=0.02, rely=0.95, anchor="sw")
    btn_volver.bind("<Enter>", boton_salir_hover)
    btn_volver.bind("<Leave>", boton_salir_leave)

# ----------- INICIO ----------- #
mostrar_login()
base.mainloop()
