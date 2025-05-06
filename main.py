# Importamos la librería
import tkinter
from views.headerView import header_view
from views.formView import form_view

# Nombramos nuestra variable e importamos la librería e 
# utilizamos "tk" para crear una ventana 
ventana = tkinter.Tk()
ventana.title("Informe Base de Datos")
ventana.geometry("1000x700")

# Configuración de tamaño de pantalla
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=6)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=4)
#-------------------------------------------------------

#Paneles de la ventana 
header_view(ventana)
form_view(ventana)

ventana.mainloop() 