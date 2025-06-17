import tkinter
from tkinter import ttk
from Services.sql import conectar

def actualizarTabla(consulta_sql, panel):
    consulta = conectar(consulta_sql)

    for widget in panel.winfo_children():
        widget.destroy()

    columnas = ("id", "nombre", "genero", "placa", "color", "modelo_transporte",
                "hora_entrada", "hora_salida", "tarifa", "carwash")
    crear_tabla(panel, columnas, consulta)

def crear_tabla(panel, columnas, datos):
    tabla = ttk.Treeview(panel, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor=tkinter.CENTER)
    for dato in datos:
        tabla.insert("", tkinter.END, values=dato)
    tabla.pack(padx=10, pady=10)
    return tabla