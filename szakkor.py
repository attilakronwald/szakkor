jatekok = []  
with open('games.csv', 'r', encoding='utf-8') as adatfolyam:
    for sor in adatfolyam:
        adatok = sor.strip().split(',')
        jatek = {'id': int(adatok[0]), 'nev': adatok[1].strip(), 'fejleszto': adatok[2].strip(), 'megjelenes eve': int(adatok[3]), 'mufaj': adatok[4].strip(), 'eladott_peldanyszam': int(adatok[5]), 'osszbevetel': int(adatok[6])}
        jatekok.append(jatek)

#print(f'{jatekok=}\n')

print(f'{jatekok[0]}')

for jatek in jatekok:
    print(f"Játék neve:{jatek['nev']}\n")
    print(f"\tFejlesztő: {jatek['fejleszto']}\n")

#print(f"{jatekok['nev'][0]}")

for jatek in jatekok:
    if jatek['id'] == 34:
        print(f"{jatek['nev']}")

for jatek in jatekok:
    if jatek['megjelenes eve'] == 2015:
        print(f"{jatek['nev']}")