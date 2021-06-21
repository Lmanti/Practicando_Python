import json

# a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
# trans = str.maketrans(a,b)
# print(strjson1.translate(trans))

archivo = """{
    "jadiazcoronado":{
        "nombres": "Juan Antonio",
        "apellidos": "Díaz Coronado",
        "edad":19,
        "colombiano":true,
        "deportes":["Fútbol","Ajedrez","Gimnasia"]
    },
    "dmlunasol":{
        "nombres": "Dorotea Maritza",
        "apellidos": "Luna Sol",
        "edad":25,
        "colombiano":false,
        "deportes":["Baloncesto","Ajedrez","Gimnasia"]
    }
}"""
# archivo = input() # tambien funciona pasando el json desde consola!!

datos = json.loads(archivo)

x = input("Ingrese deporte: ")

for i in datos:
    if x in datos[i]['deportes']: print(datos[i]["nombres"], datos[i]["apellidos"])