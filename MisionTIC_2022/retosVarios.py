'''
Un agente de viajes necesita calcular el presupuesto de alojamiento de acuerdo  
con las necesidades de sus clientes. Él cuenta con una lista de datos de los requerimientos de  
sus clientes, como se muestra a continuación: 
datos = [{'id': 8533644, 'nombre': 'Nelson', 'apellido': 'Charris', 'adultos': 2, 'niños': 2, 'bebes': 0, 'estrellas': 3}, 
{'id': 32774589, 'nombre': 'Marina', 'apellido': 'Meléndez', 'adultos': 2, 'niños': 0, 'bebes': 0, 'estrellas': 3}, 
{'id': 32569874, 'nombre': 'Liliana', 'apellido': 'Obredor', 'adultos': 2, 'niños': 1, 'bebes': 1, 'estrellas': 4}, 
{'id': 8547963, 'nombre': 'Alejandro', 'apellido': 'Pérez', 'adultos': 3, 'niños': 3, 'bebes': 1, 'estrellas': 4}, 
{'id': 32478159, 'nombre': 'Ana', 'apellido': 'Cantillo', 'adultos': 1, 'niños': 0, 'bebes': 0, 'estrellas': 2}] 
El cálculo del presupuesto de alojamiento se calcula teniendo en cuenta los siguientes  
criterios: 
1. Precio por persona de la noche de alojamiento según cantidad de estrellas del hotel.  
Estrellas Precio por noche por persona 
1 $40.000 
2 $70.000 
3 $110.000 
4 $180.000 
5 $220.000 
Tabla No. 1 
2. Si la persona es un bebé, el alojamiento no tiene costo. 
3. Si la persona es un adulto, paga la tarifa plena de la Tabla No. 1. 
4. Si la persona es un niño tiene un 20% de descuento en la tarifa por persona por noche. 
5. No se aceptan más de 4 personas por habitación, es decir que, si la cantidad de  
personas es 6 por ejemplo, se necesitan 2 habitaciones. 
Requerimiento. Escriba una función que permita al agente de viajes calcular el presupuesto  
de viajes de sus clientes por noche y cuántas habitaciones necesitan según la cantidad de  
personas. La función debe recibir como parámetros la lista datos descrita anteriormente y la  
identificación del cliente. Se debe devolver un diccionario que contenga el nombre y apellido del cliente, el presupuesto por noche, la cantidad de personas y la cantidad de habitaciones  
que necesita de acuerdo con los criterios establecidos anteriormente.  
Nota: para la solución del reto no está permitido el uso de funciones como filter o map.
'''

datos = [{'id': 8533644, 'nombre': 'Nelson', 'apellido': 'Charris', 'adultos': 2, 'niños': 2, 'bebes': 0, 'estrellas': 3}, 
{'id': 32774589, 'nombre': 'Marina', 'apellido': 'Meléndez', 'adultos': 2, 'niños': 0, 'bebes': 0, 'estrellas': 3}, 
{'id': 32569874, 'nombre': 'Liliana', 'apellido': 'Obredor', 'adultos': 2, 'niños': 1, 'bebes': 1, 'estrellas': 4}, 
{'id': 8547963, 'nombre': 'Alejandro', 'apellido': 'Pérez', 'adultos': 3, 'niños': 3, 'bebes': 1, 'estrellas': 4}, 
{'id': 32478159, 'nombre': 'Ana', 'apellido': 'Cantillo', 'adultos': 1, 'niños': 0, 'bebes': 0, 'estrellas': 2}]

precios = [40000, 70000, 110000, 180000, 220000]

for persona in datos:
    # print(persona)
    ocupantes = persona['adultos'] + persona['niños'] + persona['bebes']
    habitaciones = 1
    precioNoche = precios[persona['estrellas'] - 1]
    precioConDescuento = int(precioNoche - (precioNoche * 0.20))
    presupuesto = (persona['adultos'] * precioNoche) + (persona['niños'] * precioConDescuento)
    while ocupantes / 4 > 1: 
        habitaciones += 1
        ocupantes -= 4
    
    print(f'El presupuesto total es de: ${str(presupuesto)} y necesitará {habitaciones} habitaciones.')