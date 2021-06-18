import json

# data = {
#     "cientifico": {
#         "nombre": "Alan Mathison Turing",
#         "edad": "41"
#     }
# }

# with open("C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/data_file.json", "w") as write_file:
#     json.dump(data, write_file)

#     json_string = json.dumps(data)
# print(json_string, type(json_string))

###### indentando el json ######

#     json_string = json.dumps(data, indent=4)
# print(json_string, type(json_string))

# with open("C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/data_file.json", "r") as read_file:
#     data = json.load(read_file)
# print(data["cientifico"])

# json_string = ''' {"cientifico": {"nombre": "Alan Mathison Turing", "edad": "41"}} '''
# data = json.loads(json_string)
# print(data)

# from pprint import pprint
# strjson = '''{
#         "boolean1": null,
#         "diccionario": {"papa": 2000, "arroz": 5000},
#         "intValue": 0, 
#         "myList": [],
#         "myList2":["info1", "info2"],
#         "littleboolean": false,
#         "myEmptyList": null,
#         "text1": null,
#         "text2": "hello",
#         "value1": null,
#         "value2": null
#     }'''

# data = json.loads(strjson)
# pprint(data)
# print(data["text2"], type(data["text2"]))
# print(data["text1"], type(data["text1"]))
# print(data["intValue"], type(data["intValue"]))
# print(data["myList"], type(data["myList"]))
# print(data["myList2"], type(data["myList2"]))
# print(data["diccionario"], type(data["diccionario"]))
# print(data["myList2"][1])
# print(data["diccionario"]["papa"])

import requests
# from pprint import pprint

response = requests.get('https://jsonplaceholder.typicode.com/todos')
pendientes = json.loads(response.text)

# pprint(pendientes)
# print(pendientes[:2]) # los 2 primeros
# print(pendientes[-2:]) # los 2 ultimos

pendientes_por_usuario = {}
for pendiente in pendientes:
    if pendiente["completed"]:
        if pendiente["userId"] in pendientes_por_usuario: pendientes_por_usuario[pendiente["userId"]] += 1
        else: pendientes_por_usuario[pendiente["userId"]] = 1
# print(pendientes_por_usuario)
item_ordenados = sorted(pendientes_por_usuario.items(), key=lambda x: x[1], reverse=True)
# print(item_ordenados)
maximas_tareas_completadas = item_ordenados[0][1]
# print(maximas_tareas_completadas)
usuarios = []
for usuario, num_tareas_completadas in item_ordenados:
    if num_tareas_completadas == maximas_tareas_completadas:
        usuarios.append(str(usuario))
    else: break
# print(usuarios)
usuarios_con_max = " y ".join(usuarios)
# print('Los usuarios', usuarios_con_max, 'han completado', maximas_tareas_completadas, 'tareas.')

def filtro(pendiente):
    esta_completa = pendiente["completed"]
    esta_en_el_maximo_conteo = str(pendiente["userId"]) in usuarios
    return esta_completa and esta_en_el_maximo_conteo

with open("C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/tareas_filtradas.json", "w") as archivo_salida:
    tareas_filtradas = list(filter(filtro, pendientes))
    json.dump(tareas_filtradas, archivo_salida, indent=2)