import random
szamlista = []
kerekitettlista = []

for x in range(200):
    szamlista.append(random.random())
    
for x in szamlista:
    kerekitettlista.append(round(x, 0))
    
print(kerekitettlista)

db = 0  
for i in range(len(kerekitettlista) -2):
    if kerekitettlista[i] == 1 and kerekitettlista[i + 1] == 1 and kerekitettlista[i+2]:
        db += 1
    
print(db)