import tkinter
from views.datosView import actualizarTabla

def form_view(ventana):
    formulario_panel = tkinter.Frame(ventana, bg="blue", width="300", height="600") 
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

    actualizarTabla(f"SELECT * FROM datos_generales", tabla_panel)

    boton = tkinter.Button(formulario_panel, text="Enviar", command=funcion_boton)
    boton.pack(pady=5)