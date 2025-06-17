import tkinter
from views.datosView import actualizarTabla
import tkinter.messagebox as messagebox

def form_view(ventana):
    formulario_panel = tkinter.Frame(ventana, bg="Blue", width="300", height="600") 
    formulario_panel.grid(row=1, column=0, sticky="nsew")

    tabla_panel = tkinter.Frame(ventana, bg="white", width="10", height="10")
    tabla_panel.grid(row=1, column=1, sticky="nsew")

    titulo = tkinter.Label(formulario_panel, text="Formulario de registro")
    titulo.pack(pady=5)

    entry = tkinter.Entry(formulario_panel)
    entry.pack(pady=5)

    def funcion_boton():
        respuesta = entry.get()
        actualizarTabla(f"SELECT * FROM datos_generales WHERE color ='{respuesta}'", tabla_panel)

    boton = tkinter.Button(formulario_panel, text="Enviar", command=funcion_boton)
    boton.pack(pady=5)

    # HORA
    titulo = tkinter.Label(formulario_panel, text="Filtrar por hora")
    titulo.pack(pady=5)

    entry_hora1 = tkinter.Entry(formulario_panel)
    entry_hora1.pack(pady=5)

    entry_hora2 = tkinter.Entry(formulario_panel)
    entry_hora2.pack(pady=5)

    def filtrar_por_hora():
        h1 = entry_hora1.get().strip()
        h2 = entry_hora2.get().strip()

        if not h1.isdigit() or not h2.isdigit():
            messagebox.showerror("Error ingresa hora valida")
            return

        h1 = int(h1)
        h2 = int(h2)

        if h1 > h2:
            messagebox.showerror("Error", "La hora inicial no puede ser mayor que la final")
            return

        h1_formato = f"{h1:02d}:00"
        h2_formato = f"{h2:02d}:00"

        consulta = f"SELECT * FROM datos_generales WHERE hora_entrada BETWEEN '{h1_formato}' AND '{h2_formato}'"
        actualizarTabla(consulta, tabla_panel)

    boton_hora = tkinter.Button(formulario_panel, text="Enviar", command=filtrar_por_hora)
    boton_hora.pack(pady=5)

    # FILTRO DE TARIFA DINÁMICO (mayor o menor a un valor)
    titulo_tarifa = tkinter.Label(formulario_panel, text="Filtrar por tarifa")
    titulo_tarifa.pack(pady=5)

    entry_tarifa = tkinter.Entry(formulario_panel)
    entry_tarifa.pack(pady=5)

    def filtrar_tarifa_mayor():
        valor = entry_tarifa.get()
        if not valor.replace(".", "", 1).isdigit():
            messagebox.showerror("Error", "La tarifa debe ser un número.")
            return
        consulta = f"SELECT * FROM datos_generales WHERE tarifa > {valor}"
        actualizarTabla(consulta, tabla_panel)

    def filtrar_tarifa_menor():
        valor = entry_tarifa.get()
        if not valor.replace(".", "", 1).isdigit():
            return
        consulta = f"SELECT * FROM datos_generales WHERE tarifa < {valor}"
        actualizarTabla(consulta, tabla_panel)

    boton_tarifa_mayor = tkinter.Button(formulario_panel, text="Tarifa > valor", command=filtrar_tarifa_mayor)
    boton_tarifa_mayor.pack(pady=5)

    boton_tarifa_menor = tkinter.Button(formulario_panel, text="Tarifa < valor", command=filtrar_tarifa_menor)
    boton_tarifa_menor.pack(pady=5)

    # Filtro de género (Masculino/Femenino)
    titulo_genero = tkinter.Label(formulario_panel, text="Filtrar por género (Masculino/Femenino)")
    titulo_genero.pack(pady=5)

    entry_genero = tkinter.Entry(formulario_panel)
    entry_genero.pack(pady=5)

    def filtrar_por_genero():
        genero = entry_genero.get().strip().lower()

        if genero not in ["masculino", "femenino"]:
            messagebox.showerror("Error", "Por favor ingrese 'Masculino' o 'Femenino'.")
            return

        # Mostrar los registros que coincidan con 'Masculino' o 'Femenino'
        consulta = f"SELECT * FROM datos_generales WHERE genero = '{genero.capitalize()}'"
        print("Consulta SQL:", consulta)  # Esto imprime la consulta para que puedas verificarla
        actualizarTabla(consulta, tabla_panel)

    boton_genero = tkinter.Button(formulario_panel, text="Filtrar por género", command=filtrar_por_genero)
    boton_genero.pack(pady=5)

    # Cargar los datos iniciales
    actualizarTabla(f"SELECT * FROM datos_generales", tabla_panel)

    return formulario_panel



    