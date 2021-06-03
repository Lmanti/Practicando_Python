# ejercicio 1
# p = int(input('Ingrese número de hojas por rama: '))
# k = int(input('Ingrese número de ramas cortadas en cada arbol por igual: '))
# t = int(input('Ingrese el total de hojas que se deben obtener: '))

# arboles = t / (k * p)

# print('se necesitan', arboles, 'arboles')

# ejercicio 2
k = int(input('Ingrese el monto prestado: '))
i = float(input('Ingresa el interes: '))
t = 7

iS = k + ((k * (i / 100)) * t)
iC = k * (1 + i / 100)**t

print('En una semana pagaré $' + str(iS) + ' pesos si es interes simple')
print('En una semana pagaré $' + str(iC) + ' pesos si es interes compuesto')