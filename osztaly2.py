class ember:
    def __init__(self, nev, eletkor, varos, magassag, suly, foglalkozas):
        self.nev = nev
        self.eletkor = eletkor
        self.varos = varos
        self.magassag = magassag  
        self.suly = suly
        self.foglalkozas = foglalkozas

    def bemutatkozas(self):
        return (f"Szia, {self.nev} vagyok, {self.eletkor} éves, \n"
                f"{self.varos}ból. {self.magassag} cm magas és {self.suly} kg súlyú. \n"
                f"Foglalkozásom: {self.foglalkozas}.")