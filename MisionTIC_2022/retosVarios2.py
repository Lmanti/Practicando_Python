def conversion(datos):
    tempC = list(map(lambda x: round(((1.1 * x * 100.0) / 1024.0), 1), datos))
    mayorOIgualQue40 = []
    menorQue40 = []
    for i in tempC:
        if i >= 40: mayorOIgualQue40.append(i)
        else: menorQue40.append(i)
    print([mayorOIgualQue40, len(mayorOIgualQue40), menorQue40, len(menorQue40)])

datos = (224, 216, 296, 204, 324, 360, 379, 
335, 299, 328, 267, 248, 399, 393, 280, 211, 
341, 433, 238, 206, 301, 209, 309, 391, 220, 
296, 402, 347, 312, 321, 252, 347, 269, 318, 
205, 211, 261, 345, 395, 309, 347, 222, 351, 
272, 222, 356, 386, 259, 428, 304, 205, 314, 
371, 416, 249, 322, 333, 328, 430, 393, 347, 
232, 349, 275, 405, 243, 271, 342, 415, 422, 
205, 291)

conversion(datos)