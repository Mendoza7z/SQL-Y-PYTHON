import tkinter
import os
from PIL import Image, ImageTk

def header_view(ventana):
    header_panel = tkinter.Frame(ventana, bg="white", height=50)
    header_panel.grid(row=0, column=0, columnspan=2, sticky="nsew")
    header_panel.grid_propagate(False)

    ruta_logo = os.path.join(os.path.dirname(__file__), "logo.png")
    try:
        imagen = Image.open(ruta_logo)
        imagen = imagen.resize((100, 100))  # Ajusta el tamaño si es necesario
        logo = ImageTk.PhotoImage(imagen)
        logo_label = tkinter.Label(header_panel, image=logo, bg="white")
        logo_label.image = logo
        logo_label.pack(side="right", padx=5, pady=5)
    except Exception as e:
        print(f"Error cargando imagen: {e}")
        logo_label = tkinter.Label(header_panel, text="[Logo]", bg="white")
        logo_label.pack(side="right", padx=5, pady=5)

    titulo = tkinter.Label(header_panel, text="Informe Base de Datos", font=("Arial", 16), bg="white")
    titulo.pack(side="left", padx=10)

    return header_panel
