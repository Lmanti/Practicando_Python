# elSeñor = "es mi pastor" + " " + "y nada me faltará"
# print("El señor: " + elSeñor)

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data.txt', 'r') as f:
#     data = f.read()
#     print(data)

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/wdata.txt', 'w') as f:
#   data = 'Estamos escribiendo en el archivo 123\n'
#   f.write(data)
#   f.write(data)
#   f.write(data)
# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/wdata.txt', 'r') as rf:
#   data = rf.read()
#   print(data)

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/wdata.txt', 'a') as f:
#   data = 'mas cosas\n'
#   f.write(data)
#   f.write(data)
#   f.write(data)
# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/wdata.txt', 'r') as rf:
#   data = rf.read()
#   print(data)

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data1.txt', 'r') as f:
#   print(f.read())

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data1.txt', 'r', encoding = 'utf-8') as f:
#   print(f.read())

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data1.txt', 'r', encoding = 'utf-8') as f:
#   linea1 = f.read(6)
#   linea2 = f.read(10)
# print(linea1)
# print(linea2)

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data1.txt', 'r', encoding = 'utf-8') as f:
#   linea1 = f.readline()
#   linea2 = f.readline()
# print(linea1, end='')
# print(linea2, end='')

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data1.txt', 'r', encoding = 'utf-8') as f:
#     print('Nombre del archivo:', f.name)
#     lista = f.readlines()
#     print(lista)

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data1.txt', 'r', encoding = 'utf-8') as f:
#   for line in f:
#     print(line, end='')

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data2.txt', 'a+', encoding = 'utf-8') as f:
#   f.write('\nEsta es la linea4: abcabcabc')
# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data2.txt', 'r', encoding = 'utf-8') as rf:
#   print(rf.read())

# values = [1234, 5678, 9012, 3.14159265, False]
# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data3.txt', 'w+') as f:
#   for value in values:
#     str_value = str(value)
#     f.write(str_value)
#     f.write('\n')
# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data3.txt', 'r', encoding = 'utf-8') as rf:
#   print(rf.read())

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data4.txt', 'r', encoding = 'utf-8') as f:
#   f.seek(11, 0) #el segundo parametro solo acepta 0: puntero, 1: principio, 2: final
#   for line in f:
#     print(line, end='')

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data4.txt', 'a+') as f:
#   print(f.tell())

# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data5.txt', 'r', encoding='utf-8') as f:
#   list_content = f.readlines()
# list_content.insert(1, 'esta es la linea 1.5: jajaja\n')
# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data5.txt', 'w', encoding='utf-8') as f:
#   contenido = ''.join(list_content)
#   f.write(contenido)
# with open('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/data5.txt', 'r', encoding='utf-8') as f:
#   print(f.read())

# import os

# entries = os.scandir('C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/')

# for entry in entries:
#     print(entry.name + ", es directorio: " + str(entry.is_dir()) + ", size: " + str(entry.stat().st_size) + " bytes.")

# import pickle

# name = ["mohit", "bhaskar", "manish"]
# skill = ["Python", "Python", "Java"]
# dict1 = dict([(k, v) for k, v in zip(name, skill)])
# with open("C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/programming_powers.pkl", "wb") as p_file:
#     pickle.dump(name, p_file)
#     pickle.dump(skill, p_file)
#     pickle.dump(dict1, p_file)
# with open("C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/programming_powers.pkl", "rb") as p_file:
#     list1 = pickle.load(p_file)
#     list2 = pickle.load(p_file)
#     dict1 = pickle.load(p_file)
# print(list1)
# print(list2)
# print(dict1)

# with open("C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/discurso.jpg", "rb") as imagen:
#     data = imagen.read()
# with open("C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/copy.jpg", "wb") as f:
#     f.write(data)

'''
1. Dado el archivo de texto files/SalesJan2009.csv, procese el archivo para obtener las compras realizadas en un pa ́ıs dado.
'''

with open("C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/SalesJan2009.csv") as db:

    lista = db.readlines()

def ventasPorPais(pais: str):
        count = 0
        for sale in lista:
            if pais.lower() in sale.lower(): count += 1
        print(count)

x = input("Ingrese pais: ")

ventasPorPais(x)

'''
2. Dado el archivo de texto files/SalesJan2009.csv, procese el archivo para obtener las compras realizadas con un medio de pago dado.
'''

def ventasPorMedioDePago(medioDePago: str):
        count = 0
        for sale in lista:
            if medioDePago.lower() in sale.lower(): count += 1
        print(count)

y = input("Ingrese medio de pago: ")

ventasPorMedioDePago(y)