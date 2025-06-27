import tkinter as tk
from tkinter import messagebox

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
frame_borrarTorneo = tk.Frame(base, bg=COLOR_FONDO)
frame_jugar = tk.Frame(base, bg=COLOR_FONDO)
frame_stats = tk.Frame(base, bg=COLOR_FONDO)

# ----------- FUNCIONES DE PANTALLAS ----------- #
def ocultar_todos():
    for f in [frame_login, frame_menu, frame_crearPers, frame_borrarPers,
    frame_crearTorneo, frame_borrarTorneo, frame_jugar, frame_stats]:
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
        with open("Proyecto#3/acceso.txt", "r", encoding="utf-8") as acceso:
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

def existe_alter_ego(alter_ego, archivo="Proyecto#3/personajes.txt"):
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(";")
            if len(partes) > 3 and partes[3].lower() == alter_ego.lower():
                return True
    return False

def guardar_personaje(personaje, archivo="Proyecto#3/personajes.txt"):
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
def borrar_personaje_por_alter_ego(alter_ego, archivo="Proyecto#3/personajes.txt"):
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
