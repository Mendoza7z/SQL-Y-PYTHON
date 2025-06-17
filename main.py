import tkinter
from views.headerView import header_view
from views.entradasView import entrada_view

ventana = tkinter.Tk()
ventana.title("Informe Base de Datos")
ventana.geometry("1000x700")

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=6)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=4)

header_view(ventana)
entrada_view(ventana)

ventana.mainloop()