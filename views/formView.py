import tkinter
from tkinter import messagebox  # <- ¡importar esto!
from views.datosView import actualizarTabla

def form_view(ventana):
    formulario_panel = tkinter.Frame(ventana, bg="Green", width="300", height="600") 
    formulario_panel.grid(row=1, column=0, sticky="nsew")

    tabla_panel = tkinter.Frame(ventana, bg="white", width="50", height="60") 
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

#------------------------------------------------------------------------------------------------------
    titulo = tkinter.Label(formulario_panel, text="Formulario de hora")
    titulo.pack(pady=5)

    entry_hora1 = tkinter.Entry(formulario_panel)
    entry_hora1.pack(pady=5)

    entry_hora2 = tkinter.Entry(formulario_panel)
    entry_hora2.pack(pady=5)

    def filtrar_hora():
        h1 = entry_hora1.get().strip()
        h2 = entry_hora2.get().strip()

        if not h1.isdigit() or not h2.isdigit():
            messagebox.showerror("Error", "Las horas deben ser valores numéricos.")
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

    boton_hora = tkinter.Button(formulario_panel, text="Enviar", command=filtrar_hora)
    boton_hora.pack(pady=5)

    actualizarTabla(f"SELECT * FROM datos_generales", tabla_panel)


#------------------------------------------------------------------------------------------------------    
    titulo_genero = tkinter.Label(formulario_panel, text="Formulario de genero")
    titulo_genero.pack(pady=5)

    entry_genero = tkinter.Entry(formulario_panel)
    entry_genero.pack(pady=5)

    def filtrar_genero():
        genero = entry_genero.get().strip().capitalize()
        if genero not in ["Masculino", "Femenino"]:
            tkinter.messagebox.showerror("Error", "Ingrese 'Masculino' o 'Femenino'")
            return

        consulta = f"SELECT * FROM datos_generales WHERE genero = '{genero}'"
        actualizarTabla(consulta, tabla_panel)

    boton_genero = tkinter.Button(formulario_panel, text="Enviar", command=filtrar_genero)
    boton_genero.pack(pady=5)

#------------------------------------------------------------------------------------------------------
    titulo_modelo = tkinter.Label(formulario_panel, text="Formulario de modelo")
    titulo_modelo.pack(pady=5)

    entry_modelo = tkinter.Entry(formulario_panel)
    entry_modelo.pack(pady=5)

    def filtrar_modelo():
        modelo = entry_modelo.get().strip().capitalize()
        consulta = f"SELECT * FROM datos_generales WHERE modelo_transporte = '{modelo}'"
        actualizarTabla(consulta, tabla_panel)

    boton_modelo = tkinter.Button(formulario_panel, text="Enviar", command=filtrar_modelo)
    boton_modelo.pack(pady=5)


    return formulario_panel
