try:
    a = int("abc")
except ValueError:
    print("Nem alakithato számmá")
except TypeError:
    print("Tipushiba")