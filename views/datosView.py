import tkinter
from Services import conectar

def actualizarTabla(consulta_sql, panel):
    
    consulta  = conectar(consulta_sql)

    for cada_fila in consulta:
       for cada_columna in cada_fila:
           celda = tkinter.Label(panel,text=cada_columna,font=("Verdana", 12), fg="navy blue", bg="white")
           celda.pack()
