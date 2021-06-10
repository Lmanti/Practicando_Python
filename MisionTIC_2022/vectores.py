# def lee_arregloenteros():
#     return [int(x) for x in input('Arreglo: ').split()]

# print(lee_arregloenteros())

# def lee_arregloenteros():
#     return [int(x) for x in input('Arreglo: ').split(', ')]

# print(lee_arregloenteros())

# def suma_arreglo(arr):
#     sum = 0
#     for x in arr:
#         sum += x
#     return sum

# print(suma_arreglo([1, -3, 4, 11, 6]))

# def pos_maximo(arr):
#     max = 0
#     for i in range(1, len(arr)):
#         if arr[i] > arr[max]:
#             max = i
#     return max

# print(pos_maximo([1, -3, 4, 11, 6]))

# def cuadrados_matriz(x):
#     y = []
#     for i in range(len(x)):
#         fila = []
#         for j in range(len(x[i])):
#             fila.append(x[i][j] * x[i][j])
#         y.append(fila)
#     return y

# print(cuadrados_matriz([[1, -3, 2], [4, 11, -1]]))

# def diagonal_matriz(x):
#     y = []
#     for i in range(len(x)):
#         y.append(x[i][i])
#     return y

# print(diagonal_matriz([[1, -3], [4, 11]]))


# def diagonal_matriz(x):
#     y = []
#     for i in range(len(x)):
#         y.append(x[i - 1][i - 2])
#     return y

# print(diagonal_matriz([[1, -3], [4, 11]]))

def matriz_simetrica(x):
    bandera = True
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            bandera = bandera and (x[i][j] == x[j][i])
    return bandera

print(matriz_simetrica([[1, -3], [4, 11]]))
print(matriz_simetrica([['A', 'B'], ['B', 'A']]))