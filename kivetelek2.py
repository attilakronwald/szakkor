try:
    lista = [1, 2, 3]
    print(lista[5]) # Ez IndexError-t okoz
    print(10 / 0)   # Ez ZeroDivisionError-t okoz
except (IndexError, ZeroDivisionError) as error:
    print(f"Hiba: {error}")