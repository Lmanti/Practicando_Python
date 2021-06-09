# lista1 = [0, 1, 2, 3]
# lista2 = ['A', 'B', 'C']
# lista3 = [lista1, lista2]
# print(lista3)
# print(lista3[0])
# print(lista3[1])
# print(lista3[1][0])

# lista1 = ["A", "B", "C", "E"]
# lista2 = [1, 2, 3, 4, 5]
# lista3 = lista1 + lista2 # aqui se presenta un pequeño error
# print(lista3)

# nombres = ['Antonio', 'María', 'Mabel']
# otros_nombres = ['Barry', 'John', 'Guttag']
# nombres.extend(otros_nombres)
# print(nombres)
# print(otros_nombres)

# lista1 = [1, 2, 3, 4, 5]
# lista2 = lista1 * 3
# print(lista2)
# lista3 = ['Abc', 'Bcd']
# lista4 = lista3 * 2
# print(lista4)

# print(['Rojas', 123] < ['Rosas', 123])
# print(['Rosas', 123] == ['rosas', 123])
# print(['Rosas', 123] > ['Rosas', 23])
# print(['Rosas', '123'] > ['Rosas', '23'])

# avengers = ['Ironman', 'Thor', 'Ant-man', 'Hulk']
# print(avengers[0])
# print(avengers[3])
# print(avengers[-1])
# print(avengers[-3])

# text = ['cien', 'años', 'de', 'soledad']
# if 'años' in text: print('Si está')
# else: print('No está')

# s = ['hola', 'amigos', 'mios']
# for palabra in s:
#     print(palabra, end = ', ')

# d = 10
# desplaza = [d + x for x in range(5)]
# print(desplaza)
# potencias = [3 ** x for x in range(2, 6)]
# print(potencias)

# lista = [1, -2, 3]
# a, b, c = lista
# print('a =', a)
# print('b =', b)
# print('c =', c)

# lista = [11, 9, -2, 3, 8, 5]
# var1, var2, var3 = [lista[i] for i in (1, 3, 5)]
# print('var1 =', var1, 'var2 =', var2, 'var3 =', var3)
# var1, var2, var3 = [lista[i] for i in range(0, 6, 2)]
# print('var1 =', var1, 'var2 =', var2, 'var3 =', var3)

# def minmax(a, b):
#     if a < b: return [a, b]
#     else: return [b, a]

# x, y = minmax(5, 13)
# print('min =', x,',', 'max =', y)
# x, y = minmax(12, -4)
# print('min =', x,',', 'max =', y)

# lista = ['E', 'l', 'm', 'e', 'j', 'o', 'r']
# lista[0] = 'e'
# print(lista)
# lista[4] = 'l'
# print(lista)
# lista[-1] = 's'
# print(lista)

# print(list('hola'))

# nombres = ['Antonio', 'Johan']
# nombres.append('Mónica')
# print(nombres)
# nombres.append('María')
# print(nombres)
# nombres.append('Mabel')
# print(nombres)

# nombres = ['Antonio', 'Johan', 'María']
# nombres.insert(0, 'Mónica')
# print(nombres)
# nombres.insert(2, 'Peter')
# print(nombres)
# nombres.insert(len(nombres) // 2, '10')
# print(nombres)

# nombres = ['a', 'e', 'i', 'o', 'u', 'i', 'x']
# nombres.remove('x')
# print(nombres)
# nombres.remove('i')
# print(nombres)
# nombres.remove('i')
# print(nombres)

# avengers = ['Ironman', 'Thor', 'Ant-man', 'Hulk']
# print(avengers[:2])
# print(avengers[1:3])
# print(avengers[3:3])
# print(avengers[::-1])

# lista = [4, 3, 8, 8, 2, 5, 4, 6, 8, 9]
# print(lista.count(2))
# print(lista.count(8))
# print(lista.count(5))
# print(lista.count(7))
# print(min(lista))
# print(max(lista))

# lista = [4, 3, 8, 8, 2, 5, 4, 6, 8, 9]
# print(lista.index(2))
# print(lista.index(8))
# print(lista.index(5))

# lista = [4, 5, -1, 6, 7]
# lista.sort
# print(lista)
# lista.sort(reverse = True)
# print(lista)

# lista = ['a', 'b', 'c', 'd', 'f']
# lista.sort
# print(lista)
# lista.sort(reverse = True)
# print(lista)

nombres = ['Antonio', 'Johan', 'Mónica', 'Mabel']
nombres.pop(1)
print(nombres)
nombre_borrado = nombres.pop()
print(nombre_borrado, 'Ha sido eliminada de la lista.')
print(nombres)