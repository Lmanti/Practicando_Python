# CICLOS (while y luego for)

# 1. Imprimir cuadrado de un número mientras no sea negativo

# def cuadradoNumero(num):
#     cuadrado = 0
#     while num > 0:
#         cuadrado = num ** 2
#         num = 0
#     print(cuadrado)

# x = int(input('Ingrese un número para hallar su cuadrado: '))

# cuadradoNumero(x)

# 2. Imprimir una cosa si es par, imprmir otra si no

# def impParImp(num):
#     while num > 1:
#         if num % 2 != 0: 
#             print(3 * num + 1, end = ' ')
#             num = 3 * num + 1
#         else: 
#             print(num // 2, end = ' ')
#             num = num // 2

# x = int(input('Ingrese un número: '))
# impParImp(x)

# 3. imprimir cuando supere el pais B al A

# A = 25000000
# B = 18900000
# año = 2022
# while B < A:
#     A = A + (A * 0.02)
#     B = B + (B * 0.03)
#     año += 1
# print(año)

# 4. imprimir Epsilon de la máquina, el número más pequeño antes de que sean iguales

# xo:float = 2
# xf:float = 0
# contador = 0
# while xo != xf:
#     xo = xf
#     xf = 1 + 2 ** contador
#     contador -= 1
#     print(xf)

# 5. imprimir un listado del 1 al 100 con su cuadrado

# for i in range(100):
#     print(i, i ** 2)

# 6. imprimir listado del 1 al 999 para impares y 2 al 1000 para pares

# for i in range(1,1000,2):
#     print(i, i - 1)

# 7. imprimir un numero ingresado decrecientemente hasta el 2

# x = int(input('Ingresa un número: '))

# for i in range(x, 1, -2):
#     print(i)

# 8. imprimir los factoriales

# x = int(input('Ingresa un número: '))
# fac = 1
# for i in range(x):
#     fac *= i + 1
#     print(i + 1, fac)

# CADENAS (STRINGS)

# descubrir si la string está contenida dentro de otra (letra por letra)

# solucion 1 (te muestra hasta la repetición de letras)
# def estaIncluida(cad1, cad2):
#     for i in cad1:
#         for j in cad2:
#             if i == j: print(j, end = '')

# solucion 2 (te dice si está)
# def estaIncluida(cad1, cad2):
#     palabra = ''
#     for i in cad1:
#         if cad2.count(i) > 0:
#             palabra += i
#     print(palabra == cad1)

# x = input('Ingrese un String: ')
# y = input('Ingrese otra String: ')
# estaIncluida(x, y)

# invertir una string

x = input('Ingrese un String: ')
print(x[::-1])