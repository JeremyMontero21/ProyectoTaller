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
base.iconbitmap("iconoWalter.ico")

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
frame_jugar02 = tk.Frame(base, bg=COLOR_FONDO)
frame_stats = tk.Frame(base, bg=COLOR_FONDO)

# ----------- FUNCIONES DE PANTALLAS ----------- #
def ocultar_todos():
    for f in [frame_login, frame_menu, frame_crearPers, frame_borrarPers,
    frame_crearTorneo, frame_crearLuchasTorneo, frame_borrarTorneo, frame_jugar, frame_jugar02, frame_stats]:
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
    borrar_torneo()

def mostrar_juego():
    ocultar_todos()
    frame_jugar.place(relwidth=1, relheight=1)
    seleccionar_torneo()

def mostrar_stats():
    ocultar_todos()
    frame_stats.place(relwidth=1, relheight=1)
    stats()

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
    for widget in frame_crearPers.winfo_children():
        widget.destroy()

    tk.Label(frame_crearPers, text="Crear Personaje", font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_ACENTO).place(relx=0.5, rely=0.05, anchor="center")

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
            crear_formulario_personaje()

    btn_guardar = tk.Button(frame_crearPers, text="Guardar", width=15, command=guardar, bg=COLOR_BOTON, font=FONT_BOTON)
    btn_guardar.place(relx=0.5, y=690, anchor="center")

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
                continue
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

    btn_volver = tk.Button(frame_borrarPers, text="Volver al menú", font=FONT_BOTON_SALIR, width=18,
        bg=COLOR_BOTON_SALIR, fg="#fff", bd=0, relief="flat", cursor="hand2", command=mostrar_menu,
        activebackground="#FF6F6F", activeforeground="#fff")
    btn_volver.place(relx=0.02, rely=0.95, anchor="sw")
    btn_volver.bind("<Enter>", boton_salir_hover)
    btn_volver.bind("<Leave>", boton_salir_leave)

#---------FUNCIONES AUXILIARES--------------#
def obtener_alter_egos():
    alter_egos = []
    with open("luchadores.txt", "r", encoding="utf-8") as luchadores:
        for linea in luchadores:
            alter_ego = linea.strip().split(";")[3]
            alter_egos.append(alter_ego)
    return alter_egos

def obtener_nombres_torneos():
    nombres_torneos = []
    with open("torneos_creados.txt", "r", encoding="utf-8") as torneos:
        for linea in torneos:
            nombre = linea.strip().split(";")[0]
            nombres_torneos.append(nombre)
    return nombres_torneos

def obtener_num_luchadores():
    num=0
    with open("luchadores.txt", "r", encoding="utf-8") as luchadores:
        for linea in luchadores:
            num=num+1
    return num

def todos_diferentes(lista):
    vistos = []
    for elem in lista:
        if elem in vistos:
            return False
        vistos.append(elem)
    return True

def listas_no_en_comun(lista1, lista2):
    for elem in lista1:
        if elem in lista2:
            return False
    return True

# ----------- FORMULARIO CREAR TORNEO EN frame_crearTorneo ----------- #
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
    for entry in [entry_nombre,entry_lugar]:
        entry.delete(0, "end")
    tk.Label(frame_crearTorneo, text="Crear Torneo", font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_ACENTO).place(relx=0.5, rely=0.1, anchor="center")

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
    elif num < cantidad*2:
        messagebox.showerror(f"Error: Solo hay {num} luchadores", f"No hay suficientes luchadores para {cantidad} luchas.")
    elif ";" in nombre or ";" in lugar:
        messagebox.showerror("Error", "El nombre y el lugar no pueden contener punto y coma (;).")
    elif modo=="programa":
        luchas_programas(cantidad)
    else:
        ocultar_todos()
        frame_crearLuchasTorneo.place(relwidth=1, relheight=1)
        for widget in frame_crearLuchasTorneo.winfo_children():
            widget.destroy()
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
    tk.Label(subframe_luchas, text="Bando 2", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL).grid(row=0, column=2, padx=20, pady=10)
    for i in range(num):
        var1 = tk.StringVar(value=alter_egos[0])
        opc1 = tk.OptionMenu(subframe_luchas, var1, *alter_egos)
        opc1.grid(row=i+1, column=0, padx=10, pady=5)
        opc1.config(width=53)
        entradas_bando1.append(var1)
        tk.Label(subframe_luchas, text="VS", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL).grid(row=i+1, column=1, padx=5, pady=5)
        var2 = tk.StringVar(value=alter_egos[1])
        opc2 = tk.OptionMenu(subframe_luchas, var2, *alter_egos)
        opc2.grid(row=i+1, column=2, padx=10, pady=5)
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
    for luchador in alter_egos:
        if luchador not in luchadores_bando1:
            luchadores_bando2.append(luchador)
    luchadores_bando2 = random.sample(luchadores_bando2, num)
    guardar_torneo(luchadores_bando1,luchadores_bando2)

def luchas_programas(num):
    alter_egos = obtener_alter_egos()
    luchadores_bando1 = random.sample(alter_egos, num)
    disponibles = []
    for luchador in alter_egos:
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

# ----------- FORMULARIO BORRAR TORNEO EN frame_borrarTorneo ----------- #
entry_borrar = tk.Entry(frame_borrarTorneo, width=28, font=FONT_ENTRY, bg="#fff", fg="#333", bd=2, relief="groove")
entry_borrar.place(relx=0.5, rely=0.39, anchor="center")

def borrar_torneo():
    tk.Label(frame_borrarTorneo, text="Borrar Torneo", font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_ACENTO).place(relx=0.5, rely=0.18, anchor="center")
    tk.Label(frame_borrarTorneo, text="Nombre del torneo a borrar:", font=FONT_LABEL, bg=COLOR_FONDO, fg=COLOR_TEXTO).place(relx=0.5, rely=0.34, anchor="center")
    entry_borrar.delete(0, "end")
    btn_borrar = tk.Button(frame_borrarTorneo, text="Borrar", width=15, command=borrando_torneo, bg=COLOR_BOTON, font=FONT_BOTON)
    btn_borrar.place(relx=0.5, rely=0.5, anchor="center")

def borrando_torneo():
    nombre = entry_borrar.get().strip()
    if not nombre:
        messagebox.showwarning("Sin datos", "Debes ingresar el nombre del torneo a borrar.")
    else:
        encontrado = False
        nuevas_lineas = []
        with open("torneos_creados.txt", "r", encoding="utf-8") as torneos:
            for linea in torneos:
                _nombre_ = linea.strip().split(";")[0]
                if _nombre_.lower() == nombre.lower():
                    encontrado = True
                    continue
                nuevas_lineas.append(linea)
    if not encontrado:
        messagebox.showerror("Error", f"No existe un torneo con el nombre {nombre}.")
    else:
        with open("torneos_creados.txt", "w", encoding="utf-8") as torneos:
            for linea in nuevas_lineas:
                torneos.write(linea)
        messagebox.showinfo("Éxito", f"¡El torneo {nombre} ha sido borrado correctamente!")

# ----------- FORMULARIO JUGAR TORNEO EN frame_jugar ----------- #
def seleccionar_torneo():
    for widget in frame_jugar.winfo_children():
        widget.destroy()
    tk.Label(frame_jugar, text="Jugar Torneo", font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_ACENTO).place(relx=0.5, rely=0.1, anchor="center")
    nombres_torneos = obtener_nombres_torneos()
    tk.Label(frame_jugar, text="Seleccione un torneo para jugar", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL).place(relx=0.5, rely=0.45, anchor="center")
    var = tk.StringVar(value=nombres_torneos[0])
    opc = tk.OptionMenu(frame_jugar, var, *nombres_torneos)
    opc.place(relx=0.5, rely=0.5, anchor="center")
    opc.config(width=53)

    btn_jugar = tk.Button(frame_jugar, text="Jugar", width=15,
                            command=lambda: iniciando_clases_juego(var.get()),
                            bg=COLOR_BOTON, font=FONT_BOTON)
    btn_jugar.place(relx=0.5, rely=0.6, anchor="center")

class torneo:
    def __init__(self,nombre,fecha,lugar,num_luchas,lista_luchas):
        self.nombre=nombre
        self.fecha=fecha
        self.lugar=lugar
        self.numero_luchas=num_luchas
        self.luchas=lista_luchas
        self.bando_ganador=None

class lucha:
    def __init__(self,alter_ego1,alter_ego2,personaje1,personaje2):
        self.alterego_luchador1=alter_ego1
        self.alterego_luchador2=alter_ego2
        self.luchador1=personaje1
        self.luchador2=personaje2
        self.ganador_round1=None
        self.ganador_round2=None
        self.ganador_round3=None
        self.ganador_lucha=None

def iniciando_clases_juego(nombre_torneo):
    with open("torneos_creados.txt", "r", encoding="utf-8") as torneos:
        txt = torneos.readlines()
        for linea in txt:
            partes = linea.strip().split(";")
            _nombre_ = partes[0]
            if nombre_torneo == _nombre_:
                fecha = partes[1]
                lugar = partes[2]
                num_luchas = partes[3]
                lista_bando1 = eval(partes[4])
                lista_bando2 = eval(partes[5])
                lista_luchas = []
                for i in range(len(lista_bando1)):
                    p1 = crear_personaje(lista_bando1[i])
                    p2 = crear_personaje(lista_bando2[i])
                    L = lucha(lista_bando1[i],lista_bando2[i],p1,p2)
                    lista_luchas.append(L)
                torneo_actual = torneo(_nombre_,fecha,lugar,num_luchas,lista_luchas)
                return juego(torneo_actual)

def crear_personaje(alter_ego):
    with open("luchadores.txt", "r", encoding="utf-8") as luchadores:
        txt = luchadores.readlines()
        for linea in txt:
            partes = linea.strip().split(";")
            _alter_ego_ = partes[3]
            if alter_ego == _alter_ego_:
                tipo = partes[0]
                sexo = partes[1]
                nombre = partes[2]
                speed = int(partes[4])
                fuerza = int(partes[5])
                intelig = int(partes[6])
                defensa = int(partes[7])
                magia = int(partes[8])
                telepat = int(partes[9])
                estrag = int(partes[10])
                volar = int(partes[11])
                elastic = int(partes[12])
                regenera = int(partes[13])
                return Personaje(tipo,sexo,nombre,alter_ego,speed,fuerza,intelig,defensa,magia,telepat,estrag,volar,elastic,regenera)

# ----------- FORMULARIO JUGAR TORNEO CON 3 ROUNDS POR PELEA EN frame_jugar02 ----------- #
tk.Label(frame_jugar02, text="VS", font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_ACENTO).place(relx=0.5, rely=0.5, anchor="center")
subframe_jugar01 = tk.Frame(
    frame_jugar02, bg=COLOR_BOTON, width=500, height=400,
    highlightbackground=COLOR_BOTON_HOVER, highlightthickness=6
)
subframe_jugar01.place(relx=0.2, rely=0.5, anchor="center")
subframe_jugar02 = tk.Frame(
    frame_jugar02, bg=COLOR_BOTON, width=500, height=400,
    highlightbackground=COLOR_BOTON_HOVER, highlightthickness=6
)
subframe_jugar02.place(relx=0.8, rely=0.5, anchor="center")
tk.Label(frame_jugar02, text="Bando 1", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL).place(relx=0.2, rely=0.15, anchor="center")
tk.Label(frame_jugar02, text="Bando 2", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL).place(relx=0.8, rely=0.15, anchor="center")

def juego(torneo):
    ocultar_todos()
    frame_jugar02.place(relwidth=1, relheight=1)
    luchando(torneo, 1, 0, 0, 0)

def luchando(torneo, num, i, wins_bando1, wins_bando2):
    if i < len(torneo.luchas):
        lucha = torneo.luchas[i]
        ROUND = tk.Label(frame_jugar02, text=f"Lucha {num}", font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_ACENTO)
        ROUND.place(relx=0.5, rely=0.1, anchor="center")
        label_luchador1 = tk.Label(subframe_jugar01, text=lucha.alterego_luchador1, bg=COLOR_BOTON, fg="black", font=FONT_TITULO)
        label_luchador1.place(relx=0.5, rely=0.5, anchor="center")
        label_luchador2 = tk.Label(subframe_jugar02, text=lucha.alterego_luchador2, bg=COLOR_BOTON, fg="black", font=FONT_TITULO)
        label_luchador2.place(relx=0.5, rely=0.5, anchor="center")

        def pelear_tres_rounds(round_actual, victorias1, victorias2):
            if victorias1 < 2 and victorias2 < 2 and round_actual <= 3:
                round_lbl = tk.Label(frame_jugar02, text=f"Round {round_actual}", font=FONT_LABEL, bg=COLOR_FONDO, fg=COLOR_ACENTO)
                round_lbl.place(relx=0.5, rely=0.17, anchor="center")
                def resolver_round():
                    atributos_seleccionados = atributos_aleatorios()
                    puntos1 = 0
                    puntos2 = 0
                    for nombre in atributos_seleccionados:
                        num_poder_luchador1 = getattr(lucha.luchador1, nombre)
                        num_poder_luchador2 = getattr(lucha.luchador2, nombre)
                        if num_poder_luchador1 > num_poder_luchador2:
                            puntos1 += 1
                        elif num_poder_luchador2 > num_poder_luchador1:
                            puntos2 += 1
                    if puntos1 > puntos2:
                        texto = f"Round {round_actual}: Gana {lucha.alterego_luchador1}"
                        nuevo_victorias1 = victorias1 + 1
                        nuevo_victorias2 = victorias2
                    elif puntos2 > puntos1:
                        texto = f"Round {round_actual}: Gana {lucha.alterego_luchador2}"
                        nuevo_victorias1 = victorias1
                        nuevo_victorias2 = victorias2 + 1
                    else:
                        texto = f"Round {round_actual}: Empate"
                        nuevo_victorias1 = victorias1
                        nuevo_victorias2 = victorias2
                    mensaje_round = tk.Label(frame_jugar02, text=texto, bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL)
                    mensaje_round.place(relx=0.5, rely=0.23+0.05*round_actual, anchor="center")
                    def continuar():
                        mensaje_round.destroy()
                        round_lbl.destroy()
                        pelear_tres_rounds(round_actual+1, nuevo_victorias1, nuevo_victorias2)
                    base.after(1200, continuar)
                base.after(300, resolver_round)
            else:
                if victorias1 > victorias2:
                    mensaje = tk.Label(frame_jugar02, text="¡Ganador!", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL)
                    mensaje.place(relx=0.2, rely=0.85, anchor="center")
                    escribir_resultado(lucha.alterego_luchador1, lucha.alterego_luchador2, num, lucha.alterego_luchador1, torneo.nombre)
                    nuevo_wins_bando1 = wins_bando1 + 1
                    nuevo_wins_bando2 = wins_bando2
                elif victorias2 > victorias1:
                    mensaje = tk.Label(frame_jugar02, text="¡Ganador!", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL)
                    mensaje.place(relx=0.8, rely=0.85, anchor="center")
                    escribir_resultado(lucha.alterego_luchador1, lucha.alterego_luchador2, num, lucha.alterego_luchador2, torneo.nombre)
                    nuevo_wins_bando1 = wins_bando1
                    nuevo_wins_bando2 = wins_bando2 + 1
                else:
                    mensaje = tk.Label(frame_jugar02, text="Empate", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL)
                    mensaje.place(relx=0.5, rely=0.75, anchor="center")
                    escribir_resultado(lucha.alterego_luchador1, lucha.alterego_luchador2, num, "Ninguno.", torneo.nombre)
                    nuevo_wins_bando1 = wins_bando1
                    nuevo_wins_bando2 = wins_bando2
                def limpiar_y_continuar():
                    ROUND.destroy()
                    label_luchador1.destroy()
                    label_luchador2.destroy()
                    mensaje.destroy()
                    luchando(torneo, num + 1, i + 1, nuevo_wins_bando1, nuevo_wins_bando2)
                base.after(1600, limpiar_y_continuar)
        pelear_tres_rounds(1, 0, 0)
    else:
        for widget in frame_jugar02.winfo_children():
            widget.destroy()
        if wins_bando1 > wins_bando2:
            ganador = "Bando 1"
            mensaje = f"¡GANADOR DEL TORNEO: BANDO 1!"
        elif wins_bando2 > wins_bando1:
            ganador = "Bando 2"
            mensaje = f"¡GANADOR DEL TORNEO: BANDO 2!"
        else:
            ganador = "Empate"
            mensaje = "¡TORNEO TERMINADO EN EMPATE!"
        with open("torneos.txt", "a", encoding="utf-8") as resultados:
            resultados.write(f"{torneo.nombre};{torneo.fecha};{torneo.lugar};{ganador}\n")
        tk.Label(frame_jugar02, text=mensaje, font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_ACENTO).place(relx=0.5, rely=0.4, anchor="center")
        btn_volver = tk.Button(
            frame_jugar02, text="Volver al menú", font=FONT_BOTON_SALIR, width=18,
            bg=COLOR_BOTON_SALIR, fg="#fff", bd=0, relief="flat", cursor="hand2", command=mostrar_menu,
            activebackground="#FF6F6F", activeforeground="#fff"
        )
        btn_volver.place(relx=0.5, rely=0.6, anchor="center")
        btn_volver.bind("<Enter>", boton_salir_hover)
        btn_volver.bind("<Leave>", boton_salir_leave)

def escribir_resultado(alter_ego1, alter_ego2, num_round, ganador, torneo_nombre):
    with open("luchas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{alter_ego1},{alter_ego2},{num_round},{ganador},{torneo_nombre}\n")

def atributos_aleatorios():
    atributos_disponibles = [
        'velocidad', 'fuerza', 'inteligencia', 'defensa_personal', 'magia',
        'telepatia', 'estratega', 'volar', 'elasticidad', 'regeneracion'
    ]
    seleccionados = random.sample(atributos_disponibles, 5)
    return seleccionados

# ----------- FORMULARIO ESTADÍSTICAS EN frame_stats ----------- #
def stats():
    for widget in frame_stats.winfo_children():
        widget.destroy()
    tk.Label(frame_stats, text="Estadísticas", font=FONT_TITULO, bg=COLOR_FONDO, fg=COLOR_ACENTO).pack(pady=20)
    subframe_stats = tk.Frame(frame_stats, bg=COLOR_FONDO)
    subframe_stats.pack(pady=20)
    num_torneos_jugados = sum(1 for _ in open("torneos.txt", encoding="utf-8"))
    num_luchadores = sum(1 for _ in open("luchadores.txt", encoding="utf-8"))
    num_heroes, num_villanos = 0, 0
    with open("luchadores.txt", encoding="utf-8") as luchadores:
        for linea in luchadores:
            tipo = linea.strip().split(";")[0].lower()
            if tipo == "héroe" or tipo == "heroe":
                num_heroes += 1
            elif tipo == "villano":
                num_villanos += 1
    def elemento_mas_repetido(lista):
        if not lista:
            return "-"
        max_elem = lista[0]
        max_count = 0
        for elem in lista:
            count = lista.count(elem)
            if count > max_count:
                max_count = count
                max_elem = elem
        return max_elem
    def distinguir_luchadores(lista_luchadores, tipo):
        tipo_deseado = []
        with open("luchadores.txt", "r", encoding="utf-8") as luchadores:
            lineas_txt = luchadores.readlines()
            for luchador in lista_luchadores:
                for linea in lineas_txt:
                    partes = linea.strip().split(";")
                    tipo_actual = partes[0]
                    alter_ego = partes[3]
                    if luchador == alter_ego and tipo == tipo_actual:
                        tipo_deseado.append(luchador)
                        break
        return tipo_deseado
    def obtener_ganadores_lucha():
        lista = []
        with open("luchas.txt", "r", encoding="utf-8") as luchas:
            for linea in luchas:
                partes = linea.strip().replace(",", ";").split(";")
                if len(partes) >= 4:
                    ganador = partes[3]
                    lista.append(ganador)
        return lista
    def obtener_perdedores_lucha():
        lista = []
        with open("luchas.txt", "r", encoding="utf-8") as luchas:
            for linea in luchas:
                partes = linea.strip().replace(",", ";").split(";")
                if len(partes) >= 4:
                    luchador1 = partes[0]
                    luchador2 = partes[1]
                    ganador = partes[3]
                    if luchador1 == ganador:
                        lista.append(luchador2)
                    elif luchador2 == ganador:
                        lista.append(luchador1)
        return lista
    def mas_apariciones_en_torneos(tipo_buscado):
        apariciones = {}
        with open("torneos_creados.txt", "r", encoding="utf-8") as torneos:
            for linea in torneos:
                partes = linea.strip().split(";")
                if len(partes) >= 6:
                    bando1 = eval(partes[4])
                    bando2 = eval(partes[5])
                    for luchador in bando1 + bando2:
                        with open("luchadores.txt", "r", encoding="utf-8") as luchadores:
                            for lin in luchadores:
                                p = lin.strip().split(";")
                                if len(p) >= 4 and p[3] == luchador and p[0].lower() == tipo_buscado.lower():
                                    apariciones[luchador] = apariciones.get(luchador, 0) + 1
        if apariciones:
            max_luchador = list(apariciones.keys())[0]
            max_count = 0
            for luch, count in apariciones.items():
                if count > max_count:
                    max_count = count
                    max_luchador = luch
            return max_luchador
        else:
            return "-"
    alter_egos_ganadores = obtener_ganadores_lucha()
    alter_egos_perdedores = obtener_perdedores_lucha()
    heroe_mas_ganador = elemento_mas_repetido(distinguir_luchadores(alter_egos_ganadores,"Héroe"))
    heroe_mas_perdedor = elemento_mas_repetido(distinguir_luchadores(alter_egos_perdedores,"Héroe"))
    villano_mas_ganador = elemento_mas_repetido(distinguir_luchadores(alter_egos_ganadores,"Villano"))
    villano_mas_perdedor = elemento_mas_repetido(distinguir_luchadores(alter_egos_perdedores,"Villano"))
    heroe_mas_aparece = mas_apariciones_en_torneos("Héroe")
    villano_mas_aparece = mas_apariciones_en_torneos("Villano")
    stats_data = [
        ("Cantidad de torneos realizados:", str(num_torneos_jugados)),
        ("Cantidad de Héroes creados:", str(num_heroes)),
        ("Cantidad de Villanos creados:", str(num_villanos)),
        ("Héroe con más luchas ganadas:", heroe_mas_ganador),
        ("Héroe con más luchas perdidas:", heroe_mas_perdedor),
        ("Villano con más luchas ganadas:", villano_mas_ganador),
        ("Villano con más luchas perdidas:", villano_mas_perdedor),
        ("Héroe que más aparece en torneos:", heroe_mas_aparece),
        ("Villano que más aparece en torneos:", villano_mas_aparece)
    ]
    for i, (titulo, valor) in enumerate(stats_data):
        tk.Label(subframe_stats, text=titulo, anchor="w", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FONT_LABEL, width=42).grid(row=i, column=0, padx=6, pady=4, sticky="w")
        tk.Label(subframe_stats, text=valor, anchor="w", bg=COLOR_FONDO, fg=COLOR_ACENTO if i in [3,5,7] else COLOR_TEXTO, font=FONT_LABEL, width=24).grid(row=i, column=1, padx=4, pady=4, sticky="w")

    btn_volver = tk.Button(frame_stats, text="Volver al menú", font=FONT_BOTON_SALIR, width=18,
        bg=COLOR_BOTON_SALIR, fg="#fff", bd=0, relief="flat", cursor="hand2", command=mostrar_menu,
        activebackground="#FF6F6F", activeforeground="#fff")
    btn_volver.pack(side="bottom", pady=20)
    btn_volver.bind("<Enter>", boton_salir_hover)
    btn_volver.bind("<Leave>", boton_salir_leave)

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
