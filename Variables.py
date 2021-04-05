x = 5 #No se necesita especificar de que tipo es la variable, pero si se quiere...
print(x)
x = "Luis"
print(x)
x = str(25) #constructor de string
print(x)
x = int(25) #constructor de enteros
print(x)
x = float(25) #constructor de decimales
print(x)

#Ahora para saber el tipo

x = 5
y = "hola"
print(type(x))
print(type(y))

#Se puede agregar multiples valores a multiples variables en linea

x, y, z = "manzana", 25, 13.1416
print(x)
print(y)
print(z)

#Tambien asignar el mismo valor a varias variables

x = y = z = "hola"
print(x)
print(y)
print(z)

#Tambien se pueden sacar los elementos de un array usando variables, mientras tenga la misma cantidad de datos como de variables que colocas

frutas = ["manzanas", "peras", "mangos"]
x, y, z = frutas
print(x)
print(y)
print(z)