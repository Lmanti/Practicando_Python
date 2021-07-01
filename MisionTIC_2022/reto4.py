import json

def compras(json_convertido: dict, lista: list):
    lista_resultado = []
    total = 0
    for i in lista:
        if i in json_convertido:
            lista_resultado.append(i)
            total += json_convertido[i]
    print(total)
    print(" ".join(lista_resultado))

json_repuestos = json.loads(input())
lista_compra = [x for x in input().split(" ")]

compras(json_repuestos, lista_compra)