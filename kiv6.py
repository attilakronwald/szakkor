try:
    with open('adatok.csv', 'r', encoding='utf-8') as f:
        for sor in f:
            print(sor.strip())
except FileNotFoundError:
    print("Nem talalhato a fajl")