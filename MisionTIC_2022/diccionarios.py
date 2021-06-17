# dict_ports1 = {22: "SSH", 80: "Http"}
# dict_ports2 = {53: "DNS", 443: "https"}

# print(dict_ports1)
# dict_ports1.update(dict_ports2)
# print(dict_ports1)

# dict_ports1 = {22: "SSH", 80: "Http"}
# dict_ports2 = {53: "DNS", 80: "https"}

# print(dict_ports1)
# dict_ports1.update(dict_ports2)
# print(dict_ports1)

# dict_ports1 = {22: "SSH", 80: "Http"}
# dict_ports2 = {22: 53, 443: "https"}

# print(dict_ports1)
# dict_ports1.update(dict_ports2)
# print(dict_ports1)

# a = {123: "Rojas", 87:"Rosas"} == {87: "Rosas", 123: "Rojas"}
# print(a)
# print({"Rosas": 123} != {"rosas": 123})
# b = {123: "Rosas", 87:"rojas"} == {"Rosas": 123, 87: "rojas"}
# print(b)

# puertos = {22: "SSH", 23: "Telnet", 80: "HTTP", 3306: "MySQL"}
# protocolo = puertos[22]
# print(protocolo)
# puertos[443]
a = {22: "SSH", 23: "Telnet", 80: "HTTP", 3306: "MySQL"}.items()
print(a)