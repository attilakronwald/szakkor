a = int(5)
b = str("asdasdasd")
c = bool(True)
d = 12

szamlista = [5, 6, 7, 67, 41]
szoveglista = ["sajt", "sonka", "burger", 5, 6, 7]

import random

sorsoltszlista = []
gyumilista = ["sajt", "sonka", "burger", "bacon", "paradicsom", "saláta", "szosz", "buci", "ketchup", "mayo"]

for x in range(100):
    sorsoltszlista.append(random.randint(0, 9))

print(f'Lista elemei: {sorsoltszlista}')


atalakitottlista = []
for x in sorsoltszlista:
    if x == 0:
        atalakitottlista.append(gyumilista[0])
    elif x ==  1:
        atalakitottlista.append(gyumilista[1])
    elif x ==  2:
        atalakitottlista.append(gyumilista[2])
    elif x ==  3:
        atalakitottlista.append(gyumilista[3])
    elif x ==  4:
        atalakitottlista.append(gyumilista[4])
    elif x ==  5:
        atalakitottlista.append(gyumilista[5])
    elif x ==  6:
        atalakitottlista.append(gyumilista[6])
    elif x ==  7:
        atalakitottlista.append(gyumilista[7])
    elif x ==  8:
        atalakitottlista.append(gyumilista[8])
    elif x ==  9:
        atalakitottlista.append(gyumilista[9])
    
print(f'lista elemeinek szam: {len(atalakitottlista)}'
      f'{atalakitottlista}')

if "burger" in atalakitottlista:
    print(' Burger Szerepel a listaban')
else:
    print('nem szerepel a listaban')

burgerszama = 0
for x in atalakitottlista:
    if x == 'burger':
        burgerszama += 1

print(f'Burger ennyiszer szerepel a listaban: {burgerszama}')

baconszama = 0
for x in atalakitottlista:
    if x == 'bacon':
        baconszama += 1

print(f'Bacon ennyiszer szerepel a listaban: {baconszama}')