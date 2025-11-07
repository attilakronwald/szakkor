import random
szoveglista = []

for x in range(2500):
    sorsolt = random.randint(0, 1)
    if sorsolt == 0:
        szoveglista.append("a")
    else:
        szoveglista.append('b')
        

db = 0
for i in range(len(szoveglista) -3):
    if szoveglista[i] == "a" and szoveglista[i+1] == 'b' and szoveglista[i+3] == 'a':
        db += 1
        
print(f'{db}')