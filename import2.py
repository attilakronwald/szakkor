with open('forras2.txt', "r", encoding='utf-8') as fajl:
    szoveg = fajl.read()

#A MEGOLDAS
szoveg = szoveg.replace(",", "")
szoveg = szoveg.replace(".", "")

#B MEGOLDAS
elvalasztok = [',', '.', ';', '-', '\n', '[VISSZA]', '!', ':']

#ugyanaz
for jel in elvalasztok:
    szoveg = szoveg.replace(jel, " ")

#csupa kisbetu
szoveg = szoveg.lower()
# Szavak listaba tetele szokozok alapjan
szavak = szoveg.split()




# ell 1
print(f"Szavak száma: {len(szavak)}")

# ell2

tisztitott = []

for szo in szavak:
    if szo != "":
        tisztitott.append(szo)

szavak = tisztitott

#########################################
#for x in tisztitott:
#    print(x)


abetu = []
abetu.sort()
for betu in tisztitott:
    if "a" in betu or "A" in betu:
        abetu.append(betu)


print(f"Ennyi szoban szerepel az a betu: {len(abetu)}\n"
      f"A betu szerepel a szavakban: {abetu}")

with open('dihdonyihuzzalan.txt', 'a', encoding='utf-8')as abetus:
    print(f"A betu van bennuk:{abetu}", file=abetus)

tisztitott.count('török')

torokszam = 0
for x in tisztitott:
    if x == 'török':
        torokszam += 1

torokszo = []
bbetu = []
cbetu = []
dbetu = []
bcdkezd = []

for x in tisztitott:
    if 'török' == x:
        torokszo.append(x)
    elif x[0] == "b":
        bbetu.append(x)
    elif x[0] == "c":
        cbetu.append(x)
    elif x[0] == "d":
        dbetu.append(x)
    elif x[0] == "b" and x[1] == "c" and x[2] == "d":
        bcdkezd.append(x)

print(f"Ennyiszer szerepel a török szo a listaban:{len(torokszo)}")

with open('dihdonydihhuzzaldilf.txt', 'a', encoding='utf-8') as zalus:   
    print(f"Ennyiszer van bcd a listaban: {len(bbetu + cbetu + dbetu)}")
    print(f"Ennyiszer van bcd a listaban: {len(bbetu + cbetu + dbetu)}", file=zalus)
    print(f"Ezek azok aszavak: {bbetu + cbetu + dbetu}", file=zalus)