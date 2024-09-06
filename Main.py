#Tkither
# SE USA PARA IMPORTAR LA LIBRE tkinder
import tkinter as tk

# Crear una Ventana
#Se crea una venta es ncesario la intancia del metodo
#TK de la libreria tkinker, almacena la instancia de una variable.
mi_ventana = tk.Tk()
# Sirve para llamar a la ventana y colocarle un titulo
mi_ventana.title(" Lester Mendoza")
# Funciona para darle dimension y tamaño a una ventana
mi_ventana.geometry("500x600")

# Crear un texto
# Sirve para poder llenar texto dentro de una ventana
etiqueta = tk.Label(mi_ventana, text="Hola mundo")
# Muestra la etiqueta dentro de la ventana por defecto
etiqueta.pack()
# Sirve para mostrar la ventana y se queda siempre al
#final del codigo    
mi_ventana.mainloop()
