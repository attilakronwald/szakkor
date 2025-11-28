def ellenoriz_kor(kor):
    if kor < 0:
        raise ValueError("A kor nem lehet negativ")
    return True

try:
    ellenoriz_kor(-5)
except ValueError as error:
    print(f"Hiba: {error}")