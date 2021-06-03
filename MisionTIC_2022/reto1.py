def granja(tc):
    tb = (2 * tc) + 4
    tk = (tc + tb) // 5
    print(tc, tb, tk)
    if tk >= 0 and tk <= 20: print('uno')
    elif tk >= 21 and tk <= 30: print('dos')
    elif tk >= 31 and tk <= 50: print('tres')
    else: print('cuatro')

x = int(input('Ingrese la cantidad de caballos: '))

granja(x)