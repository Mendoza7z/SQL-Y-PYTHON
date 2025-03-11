import tkinter
from datosView import actualizarTabla

def formView(ventana):
    formulario_panel = tkinter.Frame(ventana, bg="green", width="300", height="600") 
    formulario_panel.grid(row=1, column=0, sticky="nsew")

    def funcion_boton():
        respuesta = entry.get()
        print(respuesta)

    tabla_panel = tkinter.Frame(ventana, bg="sky green", width="700", height="600") 
    tabla_panel.grid(row=1, column=1, sticky="nsew")
    actualizarTabla(f"SELECT [respuesta] FROM Carros", tabla_panel)


    titulo = tkinter.Label(formulario_panel, text="Formulario de registro")
    titulo.pack(pady=5)

    entry = tkinter.Entry(formulario_panel)
    entry.pack(pady=5)

    boton = tkinter.Button(formulario_panel, text="Enviar", command=funcion_boton)
    boton.pack(pady=5)


    return formulario_panel

