class Tag:
    def __init__(self, tagszam: str, nick: str):
        self.tagszam = tagszam
        self.nick = nick

    def __str__(self) -> str:
        return f"{self.nick} (tagszám: {self.tagszam})"