import tkinter

# Es un panel dentro de una ventana, le agregamos el color, tamaño
def header_view(ventana):
    header_panel = tkinter.Frame(ventana, bg="yellow", width="1000", height="100") 
    header_panel.grid(row=0, column=0, columnspan=2, sticky="nsew")

    return header_panel
