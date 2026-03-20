from osztaly import film


with open('mozifilmek.csv', 'r', encoding='utf-8') as valasz:
    next(valasz)
    filmek = []
    for x in valasz:
        lista = x.strip().split(',')
        id = lista[0]
        title = lista[1]
        year = lista[2]
        genre = lista[3]
        director = lista[4]
        country = lista[5]
        lang = lista[6]
        dur = lista[7]
        rat = lista[8]
        musd = lista[9]

        elemek = film(id, title, year, genre, director, country, lang, dur, rat, musd)
        filmek.append(elemek)


for x in filmek:
    print(x)