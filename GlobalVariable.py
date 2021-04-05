x = "Awesome" #Toda variable creada de esta manera es una variable global, puede usarse fuera, como dentro de funciones

def prueba(): #en python una funtion se define con "def" + el nombre, parentecis y los 2 puntos, no se cierra
    x = "fantastic" #esta sería ua variable local
    print("Phython is " + x)
prueba()
print("Python is " + x)

#Si queremos crear una variable global dentro de una funcion entonces...

def prueba2():
    global z
    z = "Beautiful"
prueba2() #Notece que se invoca la función que crea la variable global primero
print("Python is " + z)

#Tambien puedes cambiar el valor de una variable global estando dentro de una función de esta manera...

y = "Awesome"
def prueba3():
    global y
    y = "fantastic"
prueba3()
print("Python is " + y)