class Konyv:
    def __init__(self, azonosito: str, cim: str, szerzo: str):
        self.azonosito = azonosito
        self.cim = cim
        self.szerzo = szerzo
        self.kolcsonozheto = True  # alapból elérhető

    def __str__(self) -> str:
        statusz = "elérhető" if self.kolcsonozheto else "kikölcsönözve"
        return f"[{self.azonosito}] {self.cim} ({self.szerzo}) - {statusz}"