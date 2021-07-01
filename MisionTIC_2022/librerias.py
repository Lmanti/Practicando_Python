# import numpy as np
# =============================================================================
# a = np.array(list(range(1, 5)))
# print(type(a))
# print(a)
# print(a.shape)
# print(a[0], a[1], a[2])
# a[0] = -4
# print(a)

# 
# b = np.array([[1,2,3,5,6], [4,5,6,7,8]])
# print(b.shape)
# print(b)
# b[0,0] = 1590
# print(b)
# print(b[0, 0], b[0, 1], b[1, 0])
# =============================================================================

# =============================================================================
# a = np.zeros((2, 3, 4))
# print(a.shape)
# print(a)
# print("----------------------------")
# b = np.ones((2, 3))
# print(b.shape)
# print(b)
# print("----------------------------")
# =============================================================================

# =============================================================================
# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(a.shape)
# print(a)
# b = a[:2, 1:3]
# print(b)
# print("------------------------")
# b[0, 0] = -11
# print(b)
# print(a)
# print(a[0,1])
# =============================================================================

# =============================================================================
# x = np.array([5, -4])
# print(x.dtype)
# 
# x = np.array([1.0, 2.0])
# print(x.dtype)
# 
# x = np.array([5, -4], dtype=np.int32)
# print(x.dtype)
# =============================================================================

# =============================================================================
# x = np.array([[1,2,5], [3,4,6]], dtype=np.longdouble)
# y = np.array([[5,6,-1], [7,8,-6]], dtype=np.longdouble)
# print("Suma:")
# print(x + y)
# print("-----")
# print(np.add(x, y))
# print("raiz cuadrada:")
# print(np.sqrt(x))
# =============================================================================

# =============================================================================
# print(np.linspace(2, 3, num=10, endpoint=True, retstep=False))
# =============================================================================

# import matplotlib.pyplot as plt
# Matplotlib plot.
# =============================================================================
# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
# =============================================================================

# =============================================================================
# x = np.linspace(0, 2, 50)
# #print(x)
# # A ́un con el OO-style, usamos ".pyplot.figure" para crear la figura.
# fig, ax = plt.subplots() # Crea la figura y los ejes.
# ax.plot(x, x, label="linear") # Dibuja algunos datos en los ejes.
# ax.plot(x, x**2, label="quadratic") # Dibuja mas datos en los ejes.
# ax.plot(x, x**3, label="cubic") # ... y algunos m ́as.
# ax.set_xlabel("x label") # Agrega un x-label a los ejes.
# ax.set_ylabel("y label") # Agrega un y-label a los ejes.
# ax.set_title("Simple Plot") # Agrega t ́ıtulo a los ejes.
# ax.legend() # Agrega una leyenda.
# =============================================================================

# =============================================================================
# names = ["group_a", "group_b", "group_c"]
# values = [3.4, 50.3, 23]
# plt.figure(figsize=(9, 3))
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle("Categorical Plotting")
# plt.show()
# =============================================================================

# =============================================================================
# dictc = {"country": ["Brazil", "Russia", "India",
# "China", "South Africa", "Colombia"],
# "capital": ["Brasilia", "Moscow", "New Dehli",
# "Beijing", "Pretoria", "Bogot ́a"],
# "area": [8.516, 17.10, 3.286, 9.597, 1.221, 1.142],
# "population": [200.4, 143.5, 1252, 1357, 52.98, 49.65] }
# import pandas as pd
# brics = pd.DataFrame(dictc)
# print(brics)
# =============================================================================

# =============================================================================
# from google.colab import files
# uploaded = files.upload() #Upload files/SalesJan2009.csv
# =============================================================================

# =============================================================================
# import pandas as pd
# ventasdf = pd.read_csv("C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/SalesJan2009.csv")
# print(ventasdf.head(3)) # cantidad de filas q quiero imprimir
# =============================================================================
###################### colocar #%% para ejecutar con jupyter, te evita descargar librerias #####################################
import pandas as pd
# from collections import Counter
ventasdf = pd.read_csv("C:/Users/Familia/Desktop/Programación/Practicando_Python/MisionTIC_2022/files/SalesJan2009.csv")
#print(ventas)
# =============================================================================
# cp = Counter(ventasdf["Country"])
# print(cp.most_common(3))
# cv = Counter(ventasdf["Payment_Type"])
# print(cv.most_common(3))
# =============================================================================

# import datetime
import matplotlib.pyplot as plt
#Reporte por fecha
ventasdf["Transaction_date"]=pd.to_datetime(ventasdf["Transaction_date"])
A = (ventasdf["Transaction_date"]
.dt.floor("d")
.value_counts()
.rename_axis("date")
.reset_index(name="num ventas"))
G=A.plot(x="date",y="num ventas",color="green",title="Ventas por fecha")
plt.show()