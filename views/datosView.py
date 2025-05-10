import tkinter
from tkinter import ttk
from Services.sql import conectar
# --------------------------------------------------------------------------------

def actualizarTabla(consulta_sql, panel):
    consulta  = conectar(consulta_sql)
   
    for widget in panel.winfo_children():
        widget.destroy()

    #Datos de ejemeplo
    columnas = ("id","nombre", "genero", "placa", "color", "modelo_transporte", "hora_entrada", "hora_salida", "tarifa", "carwash" )
    crear_tabla(panel, columnas, consulta)

#----------------------------------------------------------------------------------
def crear_tabla(panel, columnas, datos):
    # Crear el Treeview
    tabla = ttk.Treeview(panel, columns=columnas, show="headings")
    
    # Configurar los encabezados
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor=tkinter.CENTER)
    
    # Insertar los datos
    for dato in datos:
        tabla.insert("", tkinter.END, values=dato)
    
    tabla.pack(padx=10, pady=10)
    return tabla