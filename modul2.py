from datetime import date, timedelta
from modul3 import Konyv
from modul import Tag

class Kolcsonzes:
    def __init__(self, konyv: Konyv, tag: Tag, napok: int = 14):
        if not konyv.kolcsonozheto:
            raise ValueError("A könyv nem kölcsönözhető, mert már ki van véve.")

        self.konyv = konyv
        self.tag = tag
        self.kezdet = date.today()
        self.hatarido = self.kezdet + timedelta(days=napok)
        self.visszahozva = False

        # állapotváltás
        self.konyv.kolcsonozheto = False

    def visszahoz(self):
        if self.visszahozva:
            return "Ez a kölcsönzés már le van zárva."

        self.visszahozva = True
        self.konyv.kolcsonozheto = True
        return f"Visszahozva: {self.konyv.cim}"

    def keses_napok(self) -> int:
        if self.visszahozva:
            return 0
        today = date.today()
        return max(0, (today - self.hatarido).days)

    def __str__(self) -> str:
        allapot = "aktív" if not self.visszahozva else "lezárt"
        return (f"Kölcsönzés: {self.konyv.cim} -> {self.tag.nick}, "
                f"kezdés: {self.kezdet}, határidő: {self.hatarido} ({allapot})")