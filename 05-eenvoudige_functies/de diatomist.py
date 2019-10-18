# invoer
from math import pi
r = float(input('geef de straal van de kleinere cirkel : '))
R = float(input('geef de straal van de grotere cirkel : '))

# berekenen
n = 0.83 * (R**2 / r**2) - 1.9
n = n // 1
opp_klein = r**2 * pi
opp_groot = R**2 * pi
bedekkingsgraad = ((n * opp_klein) / opp_groot) * 100
bedekkingsgraad = '{:.2f}'.format(bedekkingsgraad)
n = int(n)

# uitvoer
print(str(n) + ' kleine cirkels bedekken ' + str(bedekkingsgraad) + '% van de grote cirkel')

