#mintakeresés
import random
szamlista = []

for x in range(1000):
    szamlista.append(random.randint(1, 500))
    
db = 0
for x in range(len(szamlista) -2):
    if szamlista[x] == 674 and szamlista[x+1] ==671 and szamlista[x+2] == 321:
        db += 1
        
print(db)