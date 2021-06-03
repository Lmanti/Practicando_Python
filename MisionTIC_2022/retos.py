#reto semana 2

nombre_producto = input('Ingrese el nombre del producto: ')
costo_unitario = float(input('Ingrese el costo unitario: '))
precio_venta = float(input('Ingrese el precio de venta: '))
unidades_disponibles = float(input('Ingrese las unidades disponibles: '))
ganancia = str(int((precio_venta - costo_unitario) * unidades_disponibles))

print('Producto:', nombre_producto)
print('CU: $' + str(int(costo_unitario)))
print('PVP: $' + str(int(precio_venta)))
print('Unidades Disponibles:', int(unidades_disponibles))
print('Ganancia: $' + ganancia)