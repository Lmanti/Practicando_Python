# map(int, input().split(' '))
def promedio_arreglo(arr):

    mappedList = list(map(int, arr))
    sum = 0
    for i in mappedList:
        sum += i
    return sum / len(mappedList)

x = list(input('Ingrese el arreglo: ').split(', '))
print(promedio_arreglo(x))