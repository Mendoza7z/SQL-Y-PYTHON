import tkinter as tk
from tkinter import messagebox
from Services.sql import conectar
from views.datosView import actualizarTabla

def entrada_view(ventana):
    formulario_entrada = tk.Frame(ventana, bg="Green", width=200, height=600)
    formulario_entrada.grid(row=1, column=0, sticky="nsew")

    tabla_panel = tk.Frame(ventana, bg="white")
    tabla_panel.grid(row=1, column=1, sticky="nsew")

    campos = ["Nombre", "Genero", "Placa", "Color", "Modelo", "Hora de Entrada", "Hora de Salida", "Tarifa", "Carwash"]
    entradas = {}

    for campo in campos:
        label = tk.Label(formulario_entrada, text=campo, bg="orange", fg="black", font=("Arial", 10), width=20)
        label.pack(pady=(8, 0))
        entry = tk.Entry(formulario_entrada, font=("Arial", 10), width=22)
        entry.pack(pady=(0, 5))
        entradas[campo] = entry

    def filtrar_por_campos():
        condiciones = []
        for campo, entry in entradas.items():
            valor = entry.get().strip()
            if valor:
                # Se convierte el nombre del campo a minúsculas y reemplaza espacios por guiones bajos para coincidir con columnas SQL
                columna_sql = campo.lower().replace(" ", "_")
                condiciones.append(f"{columna_sql} LIKE '%{valor}%'")

        if not condiciones:
            messagebox.showerror("Error", "Por favor llena al menos un campo para buscar.")
            return

        where_clause = " AND ".join(condiciones)
        consulta = f"SELECT * FROM datos_generales WHERE {where_clause}"
        actualizarTabla(consulta, tabla_panel)

    tk.Button(formulario_entrada, text="Guardar", command=filtrar_por_campos, width=20, height=2).pack(pady=10)

    actualizarTabla("SELECT * FROM datos_generales", tabla_panel)

    return formulario_entrada