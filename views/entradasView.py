import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Entrada")
ventana.geometry("900x600")

# Barra superior
barra_superior = tk.Frame(ventana, height=30, bg="lightgray")
barra_superior.pack(fill="x")

# Contenedor principal
contenedor = tk.Frame(ventana)
contenedor.pack(fill="both", expand=True)

# Sección izquierda con 6 cuadros
izquierda = tk.Frame(contenedor, width=300, bg="white", padx=10, pady=10)
izquierda.pack(side="left", fill="both")

# Crear los 6 cuadros (como botones o etiquetas vacías)
for fila in range(1):
    for columna in range(3):
        cuadro = tk.Label(izquierda, text=" ", bg="white", relief="solid", width=10, height=5)
        cuadro.grid(row=fila, column=columna, padx=5, pady=5)

# Sección derecha con título, campos y botón
derecha = tk.Frame(contenedor, padx=20, pady=10)
derecha.pack(side="left", fill="both", expand=True)

# Título
titulo = tk.Label(derecha, text="Título", font=("Arial", 12))
titulo.pack(anchor="w", pady=(0, 10))

# Crear 5 campos de entrada
entradas = []
for _ in range(5):
    entrada = tk.Entry(derecha, width=40)
    entrada.pack(pady=5)
    entradas.append(entrada)

# Botón pequeño
boton = tk.Button(derecha, text="  ", width=10)
boton.pack(anchor="e", pady=10)

ventana.mainloop()
