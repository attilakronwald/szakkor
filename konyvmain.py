from konyvekmodul import Konyv

konyveklista = []
with open('konyvek.csv', mode='r', encoding='utf-8') as f:
    next(f)
    for x in f:
        adatok = x.strip().split(',')
        cimek = adatok[0]
        szerzok = adatok[1]
        isbnek = adatok[2]
        megjek = adatok[3]
        oldalak = adatok[4]
        k = Konyv(cimek, szerzok, isbnek, megjek, oldalak)
        konyveklista.append(k)

cimlista = []
for konyv in konyveklista:
    cimlista.append(konyv.cim)

print(*cimlista, sep='  --  ')