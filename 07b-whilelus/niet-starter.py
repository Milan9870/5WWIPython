getal_input = float(input('Geef een getal tussen 0 en 1: '))
som = 0
getal_berekend = 1
hoeveel = 0

while som < getal_input:
    getal_berekend /= 2
    som += getal_berekend
    hoeveel += 1

print(str(hoeveel) + ' ' + str(som))


