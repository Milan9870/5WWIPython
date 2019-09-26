# invoer
b = float(input('Geef de breedte ven het veld : '))
k = float(input('Geef de lengte van het veld : '))
c = float(input('Geef het aantal kubieke meter graan per hectare : '))
r = float(input('Geef de straal van de silo : '))
h = float(input('Geef de hoogte van de silo : '))
pi = 3.14159265359

# berekening
opp = k * b
opp = opp / 10000
opbrengst = opp * c
grondvlak = pi * r**2
inhoud = grondvlak * h
aantal_silos = opbrengst // inhoud
hoe_vol = opbrengst % inhoud
hoe_vol = hoe_vol * h

aantal_silos += 1

# uitvoer
print(int(aantal_silos))
print(hoe_vol)
