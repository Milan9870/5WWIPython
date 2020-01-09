som = 0
kaart = 1

while (kaart != 0) and (som < 21):
    kaart = int(input('geef een kaart: '))
    som += kaart

if som > 21:
    print('Verbrand (' + str(som) + ')')
elif som == 21:
    print('Gewonnen!')
else:
    print('Voorzichtig gespeeld (' + str(som) + ')')
