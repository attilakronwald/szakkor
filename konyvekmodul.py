class Konyv:
    def __init__(self, cim, szerzo, isbn, megj, old):
        self.cim = cim
        self.szerzo = szerzo
        self.isbn = int(isbn)
        self.megj = int(megj)
        self.old = int(old)
        self.raktar = True
        self.ar = None

    def __str__(self):
        return f"Cím: {self.cim}, Szerző: {self.szerzo}, ISBN: {self.isbn}, Megjelenés: {self.megj}, Oldalszám: {self.old}, Raktáron: {self.raktar}, Ár: {self.ar}"