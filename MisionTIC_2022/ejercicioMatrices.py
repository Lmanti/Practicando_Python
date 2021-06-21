x = 3
y = [[11.78, 12.19, 8.67, 13.16, 4.87, 3.36, 6.65], [4.49, 11.51, 14.05, 8.29, 5.64, 8.96, 2.65], [2.67, 6.82, 6.69, 6.67, 7.85, 9.63, 8.48], [41.88, 43.98, 18.69, 26.15, 43.92, 36.9, 22.38], [32.74, 26.47, 31.34, 12.24, 40.59, 40.32, 37.45], [24.43, 10.53, 20.03, 13.79, 23.74, 39.07, 34.32]]



def investigación(Nzonas, matrices):
    i = 0
    j = i + Nzonas
    
    aptitudes = []
    z = []
    
    while j < len(matrices):
        fila1 = []
        for n in matrices[i]:
            if n > 12.5 or n < 4.0:
                fila1.append({n: "NO APTO"})
            elif (n >= 4.0 and n < 5) or (n > 10.4 and n <= 12.5):
                fila1.append({n: "MARGINALMENTE APTO"})
            elif (n >= 5.0 and n < 6.0) or (n > 8.4 and n <= 10.4):
                fila1.append({n: "MODERADAMENTE APTO"})
            elif (n >= 6.0 and n <= 8.4):
                fila1.append({n: "SUMAMENTE APTO"}) 
        aptitudes.append(fila1)
        fila2 = []
        for m in matrices[j]:
            if m < 9.84: 
                fila2.append({m: "NO APTO"})
            elif (m >= 9.84 and m <= 19.68):
                fila2.append({m: "MARGINALMENTE APTO"})
            elif (m > 19.68 and m <= 39.37):
                fila2.append({m: "MODERADAMENTE APTO"})
            elif (m > 39.37):
                fila2.append({m: "SUMAMENTE APTO"})
        aptitudes.append(fila2)
        lista = []
        for k in range(len(fila1)):
            for l in fila1[k]:
                for g in fila2[k]:
                    if fila1[k][l] == fila2[k][g]: lista.append(fila1[k][l])
                    elif fila1[k][l] == "NO APTO" or fila2[k][g] == "NO APTO": lista.append("NO APTO")
                    elif (fila1[k][l] == "MODERADAMENTE APTO" and fila2[k][g] == "MARGINALMENTE APTO") or (fila1[k][l] == "MARGINALMENTE APTO" and fila2[k][g] == "MODERADAMENTE APTO"): lista.append("MARGINALMENTE APTO")
                    elif (fila1[k][l] == "SUMAMENTE APTO" and fila2[k][g] == "MARGINALMENTE APTO") or (fila1[k][l] == "MARGINALMENTE APTO" and fila2[k][g] == "SUMAMENTE APTO"): lista.append("MARGINALMENTE APTO")
                    elif (fila1[k][l] == "SUMAMENTE APTO" and fila2[k][g] == "MODERADAMENTE APTO") or (fila1[k][l] == "MODERADAMENTE APTO" and fila2[k][g] == "SUMAMENTE APTO"): lista.append("MODERADAMENTE APTO")
        z.append(lista)     
        i += 1
        j = i + Nzonas

    contador_NA = 0
    contador_MA = 0
    contador_MOA = 0
    contador_SA = 0
    moda = []
    inmoda = []

    for lista_simple in z:
        na = lista_simple.count("NO APTO")
        ma = lista_simple.count("MARGINALMENTE APTO")
        moa = lista_simple.count("MODERADAMENTE APTO")
        sa = lista_simple.count("SUMAMENTE APTO")
        data = []
        for apt in lista_simple:
            if apt == "NO APTO": contador_NA += 1
            if apt == "MARGINALMENTE APTO": contador_MA += 1
            if apt == "MODERADAMENTE APTO": contador_MOA += 1
            if apt == "SUMAMENTE APTO": contador_SA += 1
        if na > 0: data.append(na)
        if ma > 0: data.append(ma)
        if moa > 0: data.append(moa)
        if sa > 0: data.append(sa)

        if na == max(data): moda.append("no apto")
        elif ma == max(data): moda.append("marginalmente apto")
        elif moa == max(data): moda.append("moderadamente apto")
        elif sa == max(data): moda.append("sumamente apto")

        if sa == min(data): inmoda.append("sumamente apto")
        elif moa == min(data): inmoda.append("moderadamente apto")
        elif ma == min(data): inmoda.append("marginalmente apto")
        elif na == min(data): inmoda.append("no apto")        

    print(contador_NA, contador_MA, contador_MOA, contador_SA)
    print(",".join(moda))
    print(",".join(inmoda))
            
# x = int(input())
# y = []
# while len(y) < x * 2:
#     y.append([float(x) for x in input().split(' ')])

investigación(x, y)

# 3
# 11.78 12.19 8.67 13.16 4.87 3.36 6.65
# 4.49 11.51 14.05 8.29 5.64 8.96 2.65
# 2.67 6.82 6.69 6.67 7.85 9.63 8.48
# 41.88 43.98 18.69 26.15 43.92 36.9 22.38
# 32.74 26.47 31.34 12.24 40.59 40.32 37.45
# 24.43 10.53 20.03 13.79 23.74 39.07 34.32
