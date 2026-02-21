from modul3 import Konyv
from modul import Tag
from modul2 import Kolcsonzes

k1 = Konyv("K001", "A Pál utcai fiúk", "Molnár Ferenc")
k2 = Konyv("K002", "Egri csillagok", "Gárdonyi Géza")

t1 = Tag("T101", "olvaso_01")
t2 = Tag("T102", "olvaso_02")

print("Könyvek induláskor:")
print(k1)
print(k2)

print("\nKölcsönzés létrehozása:")
kolcs1 = Kolcsonzes(k1, t1, napok=14)
print(kolcs1)
print(k1)  # már nem elérhető

print("\nPróbáljuk meg ugyanazt a könyvet újra kivenni (hibát dob):")
try:
    kolcs2 = Kolcsonzes(k1, t2)
except ValueError as e:
    print("Hiba:", e)

print("\nVisszahozás:")
print(kolcs1.visszahoz())
print(k1)  # újra elérhető