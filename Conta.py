# Precio neto
# Es el precio sin iva, es quien refleja los impuestos

# Mi funcion 
def precioNormal(precio_bruto,precio_neto,IVA,):
    precio_neto = precio_Siniva / 1.12
    resultado = precio_neto * IVA
    return precio_neto, resultado

# Ejemplo 1
# Datos del producto botella de agua
Producto = "botellas de agua 600ml"
precio_Siniva = 5
precio_neto = 1.12
IVA = 0.12

precio_neto, precio_normal = precioNormal(precio_Siniva, precio_neto, IVA)

print(f"Producto: {Producto}\nProducto Siniva: Q{precio_Siniva:f}\nPrecio neto: Q{precio_neto:f}\nIVA: Q{precio_normal:f}")


# Ejemplo 2
def precioNormal1(precio_Siniva, precio_neto, IVA):
    precio_neto = precio_Siniva / 1.12
    resultado = precio_neto * IVA     
    return precio_neto, resultado

# Datos del producto Bolsas de plástico
Producto = "bolsas de plastico 100ml"
precio_Siniva = 8
precio_neto = 1.12
IVA = 0.12
precio_neto, precio_normal = precioNormal(precio_Siniva, precio_neto, IVA)

print(f"Producto: {Producto}\nProducto Siniva: Q{precio_Siniva:f}\nPrecio neto: Q{precio_neto:f}\nIVA: Q{precio_normal:f}")



