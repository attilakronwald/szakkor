class termék():
    def __init__(self, név, kat, ár, kg):
        self.név = név
        self.kat = kat
        self.ár = ár
        self.kg = 1.0


    def info(self):
        return f"{self.név}, {self.kat} kategoriaju termek és az ára {self.ár}, súlya: {self.kg}"
    
termek1 = termék("Gerpuh", "cigany", 67)
termek2 = termék("Bádonydih Huzzaldilf", "huzz", 420)

print(termek1.info())
print(termek2.info())


termek1.ár