# def tieneRepetidos(arr):
#     repetido = False
#     for i in arr:
#         if arr.count(i) > 1: repetido = True
#     print(repetido)

# x = list(input('Ingrese una lista: ').split(', '))
# tieneRepetidos(x)

# def esPalidrome(arr):
#     if arr[::-1] == arr: print('Es palídrome')
#     else: print('No es palídrome')

# x = list(input('Ingrese una lista: ').split(', '))
# esPalidrome(x)

# def contienePalidrome(arr):
#     existe = False
#     for i in arr:
#         if i[::-1] == i: existe = i
#     if not existe: print('No existe')
#     else: print(existe)

# x = list(input('Ingrese una lista: ').split(', '))
# contienePalidrome(x)

# def contieneVocalRepetida(arr):
#     existe = []
#     for i in arr:
#         if i.count('a') > 1 : existe.append(i)
#         if i.count('e') > 1 : existe.append(i)
#         if i.count('i') > 1 : existe.append(i)
#         if i.count('o') > 1 : existe.append(i)
#         if i.count('u') > 1 : existe.append(i)
#     if not existe: print('No existe')
#     else: print(', '.join(existe))

# x = list(input('Ingrese una lista: ').split(', '))
# contieneVocalRepetida(x)

# def contieneVocalRepetida(arr1, arr2):
#     resultado = []
#     for i in arr1:
#         if i in arr2: resultado.append(i)
#     if not resultado: print('Son iguales')
#     print(resultado)

# x = list(input('Ingrese la primera lista: ').split(', '))
# y = list(input('Ingrese la segunda lista: ').split(', '))
# contieneVocalRepetida(x, y)

# def promedio_arreglo(arr):

#     mappedList = list(map(int, arr))
#     sum = 0
#     for i in mappedList:
#         sum += i
#     return sum / len(mappedList)

# x = list(input('Ingrese el arreglo: ').split(', '))
# print(promedio_arreglo(x))

def calcular_producto_matriz(x):
    resultado = []
    for i in range(len(x[0])):
        resultado.append(x[0][i] * x[1][i])  
    print(resultado)

x = [int(x) for x in input('Ingrese el primer elemento de la matriz: ').split(', ')]
y = [int(y) for y in input('Ingrese el segundo elemento de la matriz: ').split(', ')]
z = [x, y]

calcular_producto_matriz(z)