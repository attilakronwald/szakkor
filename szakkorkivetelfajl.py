try:
    with open('kimenet3.txt', 'r') as adatfolyam:
        tartalom = adatfolyam.read()

    szamlista = list(map(float, tartalom.strip().split(";")))

    kettovel = []
    nemkettovel = []

    for szam in szamlista:
        if szam % 2 == 0:
            kettovel.append(szam)
        else:
            nemkettovel.append(szam)

    with open('paros.txt', 'w') as adatfolyam:
        print(f"A paros szamok: {kettovel}", file=adatfolyam)

    with open('paratlan.txt', 'w') as adatfolyam:
        print(f"A paratlan szamok: {nemkettovel}", file=adatfolyam)

except FileNotFoundError:
    print("A fajl nem talalhato")

except ValueError:
    print("Érték hiba")

finally:
    print("A txt-k letrehozva, program vege.")
