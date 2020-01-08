# invoer
aantal_basen = int(input('hoeveel basen worden er ingelezen: '))
basen = ''
verschillende_basen = 0

# berekening
for i in range(aantal_basen):
    base = input('geef een base: ')
    if base in basen:
       pass
    else:
        basen += ' ' + base
        verschillende_basen += 1


# uitvoer
if verschillende_basen == 1:
    print('De DNA-keting bevat ' + str(verschillende_basen) + ' soort base:' + basen)
else:
    print('De DNA-keting bevat ' + str(verschillende_basen) + ' verschillende soorten basen:' + basen)
