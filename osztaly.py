class film:
    def __init__(self, id, title, year, genre, director, country, lang, dur, rat, musd):
        self.id = int(id)
        self.title = str(title)
        self.year = int(year)
        self.genre = str(genre)
        self.director = str(director)
        self.country = str(country)
        self.lang = str(lang)
        self.dur = int(dur)
        self.rat = float(rat)
        self.musd = float(musd)

    def __str__(self):
        return f"ID: {self.id}\n Cím: {self.title}\n Év: {self.year}\n Műfaj: {self.genre}\n Rendező: {self.director}\n Ország: {self.country}\n Nyelv: {self.lang}\n Időtartam: {self.dur} perc\n Értékelés: {self.rat}\n Bevétel: {self.musd} millió USD\n"