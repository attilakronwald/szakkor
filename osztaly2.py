class auto:
    def __init__(self, markanev, modell, gyartasi_ev):
        self.markanev = markanev
        self.modell = modell
        self.gyartasi = gyartasi_ev
        self.sebesseg = 0
        self.motor_bekapcs = False
        self.uzemanyag_szint = 50.0
        self.kilometerora = 0


    def kiir_auto_adatok(self):
        return(f"Márka: {self.markanev}, Modell: {self.modell}, gyártási év: {self.gyartasi}, Sebesség: {self.sebesseg} km/h, Motor állapot: { 'bekapcsolva' if self.motor_bekapcs else 'kikapcsolva'}"
               f"Üzemanyagszint: {self.uzemanyag_szint} liter, Kilometerora: {self.kilometerora} km")
    
    def motorindit(self):
        if not self.motor_bekapcs and self.uzemanyag_szint > 0:
            self.motor_bekapcs = True
            return "A modul beindult."
        elif self.uzemanyag_szint <= 0:
            return "NinCSEN ELÉG üzemanyag a beinditashoz"
        return "A motor mar be van inditva"
    
    def motorleallit(self):
        if self.motor_bekapcs:
            self.motor_bekapcs = False
            self.sebesseg = 0
            return "A motor leállt"
        return "A motor le van állítva"
    
    def gyorsit(self, novekedes):
        if self.motor_bekapcs:
            self.sebesseg += novekedes
            return f"Gyorsítás: auto seb most: {self.sebesseg} km/h"
        return f"Nem lehet gyorsitani, mert a motor le van allitva"
    
    def fekez(self, csokken):
        if self.motor_bekapcs and self.sebesseg > 0:
            self.sebesseg = max(0, self.sebesseg - csokken)
            return f"Csokkenes: auto seb most: {self.sebesseg} km/h"
        return f"Nem lehet Csokkenteni, mert a motor le van allitva"
    
    def tankol(self, mennyiseg):
        self.uzemanyag_szint += mennyiseg
        return f"{mennyiseg} liter uzemanyag hozzaadva, uzemanyagszint: {self.uzemanyag_szint}"
    
    def fogyaszt(self, kilometer):
        fogyasztas = kilometer * 0.1
        self.uzemanyag_szint -= fogyasztas
        if self.uzemanyag_szint < 0:
            self.uzemanyag_szint = 0
            self.kilometerora += kilometer
        uzenet = f"Megtett tav: {kilometer}, fogy. uzemanyag: {fogyasztas}"
        if self.uzemanyag_szint == 0:
            uzenet += "Elfogyott az uzemanyag"
            self.motorleallit()
        return uzenet