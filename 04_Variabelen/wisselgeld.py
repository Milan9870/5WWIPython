# invoer
eurocent = int(input('Geef aantal eurocent: '))

# berekening
aantal_muntstukken = eurocent // 100
eurocentt = eurocent % 100

aantal_muntstukken += eurocentt // 50
eurocentt = eurocentt % 50

aantal_muntstukken += (eurocentt // 20)
eurocentt = eurocentt % 20

aantal_muntstukken += (eurocentt // 10)
eurocentt = eurocentt % 10

aantal_muntstukken += (eurocentt // 5)
eurocentt = eurocentt % 5

aantal_muntstukken += (eurocentt // 2)
eurocentt = eurocentt % 2

aantal_muntstukken += (eurocentt // 1)
eurocentt = eurocentt % 1






# uitvoer
print( str(eurocent) + ' cent kan je omwisselen in ' + str(aantal_muntstukken) + ' muntstukken')
