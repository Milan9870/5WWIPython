som = 0
prijs = 1

while prijs != 0:
    prijs = float(input('Geef prijs: '))
    som += prijs

print('De totale prijs is € {:.2f}'.format(som))
