class ember:
    def __init__(self, nev, eletkor, varos, magassag, suly, foglalkozas):
        self.nev = nev
        self.eletkor = eletkor
        self.varos = varos
        self.magassag = magassag  
        self.suly = suly
        self.foglalkozas = foglalkozas

    def bemutatkozas(self):
        print(f"Szia, {self.nev} vagyok, {self.eletkor} éves, \n"
              f"{self.varos}ból/-ből/-ról/-ről. {self.magassag} cm magas és {self.suly} kg súlyú. \n"
              f"Foglalkozásom: {self.foglalkozas}.")
    
    
    def szulinap(self):
        self.eletkor += 6

    def koltozik(self, ujvaros):
        regi_varos = self.varos
        self.varos = ujvaros

    def bmi(self):
        magassag_m = self.magassag / 100
        bmi_ertek = self.suly / (magassag_m ** 2)
        return round(bmi_ertek, 2)
    
    def hizas(self):
        self.suly += 5

    def fogyas(self):
        self.suly -= 3

    def ujmunka(self, ujfoglalkozas):
        regi_foglalkozas = self.foglalkozas
        self.foglalkozas = ujfoglalkozas

ember1 = ember("Lakatos Juan Miguel", 61, "Ózd", 210, 250, "közmunkás")
ember1.bemutatkozas()
ember1.szulinap()
ember1.koltozik("Miskolc")
ember1.hizas()
ember1.fogyas()
ember1.ujmunka("Díler")
ember1.bemutatkozas()

print(f"A BMI értéke: {ember1.bmi()}")



#ember2 = ember("Kovács Anna", 28, "Budapest", 165, 60, "programozo")
#ember2.bemutatkozas()

