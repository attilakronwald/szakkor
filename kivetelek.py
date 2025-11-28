try:
    x = int(input("Adj meg egy számot: "))
    print(f"A szám duplája: {x * 2}")
except ValueError:
    print("Hiba: Kérlek, egy számot adj meg!")