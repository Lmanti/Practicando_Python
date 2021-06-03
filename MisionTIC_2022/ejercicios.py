import math
# Vt =  4/3 πr³ + 1/3hπr².

# def Vt(re, hc, rc):
#     Ve = (4 / 3) * (math.pi * (re**3))
#     Vc = ((1 / 3) * hc) * (math.pi * (rc**2))
#     return Ve + Vc

# x1 = float(input('Ingrese el radio de la esfera\n'))
# y1 = float(input('Ingrese la altura del cono\n'))
# z1 = float(input('Ingrese el radio de la base del cono\n'))

# print('el volumen total es', Vt(x1, y1, z1))

# def At(b, a, r):
#     Ar = b * a
#     Acs = (math.pi * (r**2)) * 2
#     return Ar + Acs

# x2 = float(input('Ingrese la base de rectangulo\n'))
# y2 = float(input('Ingrese la altura del rectangulo\n'))
# z2 = float(input('Ingrese el radio de los circulos\n'))

# print('el area total total es', At(x2, y2, z2))

# def verificarNumero(num):
#     if '.' in num:
#         if float(num) > 0: print('El número', float(num), 'es positivo')
#         elif float(num) < 0: print('El número', float(num), 'es negativo')
#         else: print('El número', float(num), 'es el neutro para la suma')
#     elif num.count(',') > 0:
#         y = num.replace(',', '.')
#         if float(y) > 0: print('El número', float(y), 'es positivo')
#         elif float(y) < 0: print('El número', float(y), 'es negativo')
#         else: print('El número', float(y), 'es el neutro para la suma')
#     else:
#         if int(num) > 0: print('El número', int(num), 'es positivo')
#         elif int(num) < 0: print('El número', int(num), 'es negativo')
#         else: print('El número', int(num), 'es el neutro para la suma')

# x3 = input('Ingrese el número a evaluar: ')

# verificarNumero(x3)

# def verificarRango(r, n):
#     radio = float(r)
#     num = float(n)
#     if (num <= radio and num > 0) or (num >= -radio and num < 0): print('El punto', n, 'se encuentra dentro del rango del circulo')
#     else: print('No se encuentra el punto', n, 'dentro del rango del circulo') 

# x4 = input('Ingrese el radio del criculo: ')
# y4 = input('Ingrese en punto a evaluar: ')

# verificarRango(x4, y4)

def esTriengulo(l1, l2, l3):
    if l1 != 0 and l2 != 0 and l3 != 0: print('Se puede contruir un triangulo con las longitudes ingresadas')
    else: print('No s epuede construir un triangulo con las longitudes ingresadas')

x5 = float(input('Ingrese la primera longitud: '))
y5 = float(input('Ingrese la segunda longitud: '))
z5 = float(input('Ingrese la tercera longitud: '))

esTriengulo(x5, y5, z5)