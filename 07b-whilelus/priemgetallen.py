getal = int(input('een getal: '))
deler = 2

while deler < getal and getal % deler != 0:
    deler += 1

if deler == getal:
    print(str(getal) + ' is een priemgetal')
else:
    print(str(getal) + ' is geen priemgetal')



