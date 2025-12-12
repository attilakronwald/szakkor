from datetime import date

class ember:
    def __init__(self, nev, eletkor): #tulajdonságok, amiket megadhatok és dolgozhatok vele
        self.nev = nev #self az osztályon belüli műveletekhez van meghatározva
        self.eletkor = eletkor
    
    def koszones(self):
        return f"Szia, {self.nev} vagyok, {self.eletkor} éves."

    def szuletesiev(self):
        aktualisev = date.today().year
        return aktualisev - self.eletkor
    
    def egyevmulva(self):
        return self.eletkor + 1
    
    def novelieletkor(self):
        self.eletkor += 1
    
    def idosebb_e(self, masik_ember):
        if self.eletkor > masik_ember.eletkor:
            return f"{self.nev} idősebb, mint {masik_ember.nev}"
        elif self.eletkor < masik_ember.eletkor:
            return f"{masik_ember.nev} idősebb, mint{self.nev}"
        else:
            return "Egyidősek"

    def kategoria(self):
        if self.eletkor < 14:
            return "gyermek"
        elif self.eletkor < 65:
            return "felnőtt"
        else:
            return "Idős"
        
    def hany_ev_mulva_lesz(self, cel_eletkor):
        if cel_eletkor <= self.eletkor:
            return 0
        return cel_eletkor - self.eletkor
    
    def forditott_nev(self):
        return " ".join(self.nev.split()[::-1])

    
    def eletkorkulonbseg(self, masik_ember):
        return abs(self.eletkor - masik_ember.eletkor)
    
    def vegsokoszones(self):
        return f"Szia! {self.nev} vagyok, {self.eletkor} eves, és {self.kategoria()} kategoriába tartozom"
    
    

ember1 = ember("Anna", 30)
print(ember1.koszones())
print(ember1.szuletesiev())
masik_ember = ember("Béla", 50)
print(masik_ember.koszones())
print(masik_ember.szuletesiev())
ember3 = ember("Sándor", 40)
print(ember3.koszones())
print(ember3.szuletesiev())
