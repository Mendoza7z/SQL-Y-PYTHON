import tkinter
from PIL import Image, ImageTk

def header_view(ventana):
    hader_panel = tkinter.Frame(ventana, bg="white", width=1000, height=60)
    hader_panel.grid(row=0,column=0,columnspan=2,sticky="nsew")

    ing = Image.open("logo.png")
    ing = ing.resize((75,75))
    logo = ImageTk.PhotoImage(ing)

    logo_label = tkinter.Label(hader_panel, image=logo, bg="white")
    logo_label.image = logo
    logo_label.pack()

    logo = ImageTk.PhotoImage(Image.open("logo.png"))
