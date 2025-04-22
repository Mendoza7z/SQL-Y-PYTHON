import tkinter

def header_view(ventana):
    # Panel superior con altura 10
    header_panel = tkinter.Frame(ventana, bg="white", height=10)
    header_panel.grid(row=0, column=0, columnspan=2, sticky="nsew")
    header_panel.grid_propagate(False)

    # Logo ajustado a un tamaño intermedio
    logo = tkinter.PhotoImage(file="logo.png")
    logo = logo.subsample(2, 2)  
    logo_label = tkinter.Label(header_panel, image=logo, bg="white")
    logo_label.image = logo
    logo_label.pack(side="right", padx=5, pady=1) 

    return header_panel