#diccionarios

dict1 = {}

while len(dict1) < 3:
    dict1.update({input('Ingrese capital: '): int(input('Ingrese numero de casas: '))})

## metodo corto, con lambda ##

# dict1_sorted = sorted(dict1.items(), key = lambda x: x[1])

list_dict1 = list(dict1.items())

## con for ##

# for i in range(len(list_dict1) - 1):
#     for j in range(len(list_dict1) - 1):
#         if list_dict1[j][1] > list_dict1[j + 1][1]:
#             aux = list_dict1[j]
#             list_dict1[j] = list_dict1[j + 1]
#             list_dict1[j + 1] = aux

## con while anidado ##
for i in range(len(list_dict1) - 1):
    j = 0
    while j in range(len(list_dict1) - 1):
        if list_dict1[j][1] > list_dict1[j + 1][1]:
            aux = list_dict1[j]
            list_dict1[j] = list_dict1[j + 1]
            list_dict1[j + 1] = aux
        j += 1

print(list_dict1)