# invoer
afstand = float(input('Geef een afstand: '))
snelheid = float(input('Geef een snelheid: '))
geocentrische_gravitatieconstante = 398600.4418 * 10**9
from math import pi, sqrt

# berekenen
grote_as = (geocentrische_gravitatieconstante * afstand) / (2 * geocentrische_gravitatieconstante - afstand * (snelheid**2))
periode = 2 * pi * sqrt(grote_as**3 / geocentrische_gravitatieconstante)
minuten = periode // 60
uren = minuten // 60
minuten = minuten % 60
dagen = uren // 24
uren = uren % 24
minuten = int(minuten)
uren = int(uren)
dagen = int(dagen)

# uitvoer
print('grote as: ' + str(grote_as) + ' meter')
print('periode: ' + str(periode) + ' seconden')
print('periode: ' + str(dagen) + ' dagen, ' + str(uren) + ' uren en ' + str(minuten) + ' minuten')
