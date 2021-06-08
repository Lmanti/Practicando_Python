# def minmax(a, b):
#     if a < b: return a, b
#     else: return b, a

# x, y = minmax(5, 13)
# print(x, y)
# x, y = minmax(13, 5)
# print(x, y)

# avengers = ('Ironman', 'Thor', 'Ant-man', 'Hulk')
# print(avengers[:2])
# print(avengers[1:3])
# print(avengers[3:3])
# print(avengers[::-1])

# tupla = (4, 3, 8, 8, 2, 5, 4, 6, 8, 9)
# print(tupla.count(2))
# print(tupla.count(8))
# print(tupla.count(5))
# print(tupla.count(7))
# print(min(tupla))
# print(max(tupla))

# magician = 'Dumbledore'
# tupla = tuple(magician)
# print(tupla)

# tupla = (1, 2, 3)
# a, b, c = tupla
# print('a:', a, 'b:', b, 'c:', c)

t = tuple(map(int, input().split(' ')))
print(t)
print(t[0] + t[1])