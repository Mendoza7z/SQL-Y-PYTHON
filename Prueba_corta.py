tareas = [
    ("Estudiar para el examen", "Revisar capítulos 1 a 5", "en progreso"),
    ("Hacer ejercicio", "Ir al gimnasio por 1 hora", "completada")
]

while True:
    print("\n--- Menú ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        
        nombre = input("Nombre de la tarea: ")
        detalles = input("Detalles de la tarea: ")
        estado = input("Estado de la tarea (en progreso, completada, pendiente): ")
        tareas.append((nombre, detalles, estado))
        print("Tarea agregada.")

    elif opcion == "2":
       
        print("\n--- Tareas ---")
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea[0]} - {tarea[2]}")
        tarea_id = int(input("Número de la tarea a eliminar: ")) - 1
        if 0 <= tarea_id < len(tareas):
            tareas.pop(tarea_id)
            print("Tarea eliminada.")
        else:
            print("Número inválido.")

    elif opcion == "3":
        
        if len(tareas) > 0:
            print("\n--- Tareas ---")
            for tarea in tareas:
                print(f"Nombre: {tarea[0]}, Detalles: {tarea[1]}, Estado: {tarea[2]}")
        else:
            print("No hay tareas.")

    elif opcion == "4":
        
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
    