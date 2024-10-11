from ..services.inventario import productos
from ..controller.validar_precio import validar_precio

def actualizar_precio():
    nombre = input("Nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            nuevo_precio = input("Nuevo precio: ")
            while not validar_precio(nuevo_precio):
                nuevo_precio = input("Introduce un precio válido: ")
            producto['precio'] = float(nuevo_precio)
            print("Precio actualizado.")
            return
    print("Producto no encontrado.")