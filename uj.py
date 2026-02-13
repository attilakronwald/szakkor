from collections import Counter


with open('gerpuh.txt', 'r', encoding='utf-8') as fajl:
    szoveg = fajl.read()


kisbetu = szoveg.lower()

irasjelek = ".,!?;:\"'()-[]{}_/\\"
tisztitott_szoveg = ""

for karakter in kisbetu:
    if karakter not in irasjelek:
        tisztitott_szoveg += karakter

while "  " in tisztitott_szoveg:
    tisztitott_szoveg = tisztitott_szoveg.replace("  ", " ")

tisztitott_szoveg = tisztitott_szoveg.strip()

szavak = tisztitott_szoveg.split()

gyak = Counter(szavak)
top10szo = gyak.most_common(10)

# CSV mentés
with open('top10.csv', 'w', encoding='utf-8')as fajl:
    print(*top10szo ,sep='\n' , file=fajl)

print(*top10szo, sep='\n')
print("Mentve:", 'top10.csv')
