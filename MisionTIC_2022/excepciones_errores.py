# def division(a, b):
#     coc = a // b
#     res = a % b
#     return coc, res

# division(4, 5)
# print(division(10, 0)) # Error dividir por 0
# print(division(1024, 10))

# def division(a, b):
#     try:
#         coc = a // b
#         res = a % b
#         return coc, res
#     except:
#         print('Error en la división de', a, 'entre', b)
#         return ''

# print(division(10, 0))
# print(division(1024, 10))

# def division(a, b):
#     try:
#         coc = a // b
#         res = a % b
#         return coc, res
#     except:
#         print('Error en la división de', a, 'entre', b)

# def main():
#     try:
#         num = int(input('digite el dividendo: '))
#         div = int(input('digite el divisor: '))
#         print(division(num, div))
#     except ValueError:
#         print('El valor ingresado no es número.')

# main()

# try:
#     num = int(input('Enter the number: '))
#     re = 100 / num
# except:
#     print('Something is wrong')
# else:
#     print('result is', re)
# finally:
#     print('finally program ends')

def division(a, b):
    if b == 0:
        raise ValueError('Error de división, por cero.')
    else:
        coc = a // b
        res = a % b
        return coc, res
try:
    print(division(10, 0))
except Exception as e:
    print(e, '\n', type(e))