# Precio neto
# Es el precio sin iva, es quien refleja los impuestos

# Mi funcion 
def precioNormal(precio_bruto,precio_neto,IVA,):
    precio_neto = precio_bruto / 1.12
    resultado = precio_neto * IVA
    return precio_neto, resultado

# Ejemplo 1
# Datos del producto botella de agua
Producto = "botellas de agua 600ml"
precio_bruto = 5
precio_neto = 1.12
IVA = 0.12

precio_neto, precio_normal = precioNormal(precio_bruto, precio_neto, IVA)

print(F"Producto: {Producto}\nProducto bruto: Q{precio_bruto:f}\nPrecio neto: Q{precio_neto:f}\nIVA: Q{precio_normal:f}")


# Ejemplo 2
def precioNormal(precio_Siniva, precio_neto2, IVA):
    precio_neto2 = precio_Siniva / 1.12  
    resultado = precio_neto2 * IVA       
    return precio_neto2, resultado

# Datos del producto Bolsas de plástico
Producto2 = "bolsas de plastico 100ml"
precio_Siniva = 7
precio_neto2 = 1.12
IVA = 0.12

precio_neto, precio_normal2 = precioNormal(precio_Siniva, precio_neto2, IVA)

print(f"Producto: {Producto2}\nProducto sin IVA: Q{precio_Siniva:f}\nPrecio neto: Q{precio_neto2:f}\nIVA: Q{precio_normal2:f}")



