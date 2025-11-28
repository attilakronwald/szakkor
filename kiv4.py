try:
    file = open("adat.txt", "r")
    tartalom = file.read()
    print(tartalom)
except FileNotFoundError:
    print(f"A fajl nem talalhato")
finally:
    print(f"program vege")