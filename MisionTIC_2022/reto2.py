def compararProcesos(PR1, PR2, Ops):
    p1 = 0
    p2 = 0
    for i in Ops:
        if i in PR1: p1 += 1
        if i in PR2: p2 += 1
        if p1 > p2: print('J', end = '')
        elif p1 < p2: print('K', end = '')
        else: print('L', end = '')


x = 'AHS'
y = 'SDA'
z = 'AJSSDSAASASASSASADAJAJSS'

# x = input()
# y = input()
# z = input()

compararProcesos(x, y, z)