# x = 130

# conversion = str(x / 60)
# horas = conversion[0]
# mins = x - (60 * int(horas))

# print(horas,'h', str(mins), 'min') 


def mostrarDuracion(tiempo):
    conversion = str(tiempo / 60)
    horas = conversion.split('.')[0]
    mins = tiempo - (60 * int(horas))
    print(horas, 'h', str(mins), 'min')

x = int(input('Ingrese el tiempo en minutos a convertir: '))

mostrarDuracion(x)