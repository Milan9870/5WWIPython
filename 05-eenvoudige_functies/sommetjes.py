# invoer
getal1 = int(input('geef een willekeurig getal : '))
getal2 = int(input('geef een tweede willekeurig getal : '))

# berekenen
som1 = '{:6d} + {:<6d} = {}' .format(10**0 * getal1, 10**0 * getal2, 10**0 * (getal1 + getal2))
som2 = '{:6d} + {:<6d} = {}' .format(10**1 * getal1, 10**1 * getal2, 10**1 * (getal1 + getal2))
som3 = '{:6d} + {:<6d} = {}' .format(10**2 * getal1, 10**2 * getal2, 10**2 * (getal1 + getal2))
som4 = '{:6d} + {:<6d} = {}' .format(10**3 * getal1, 10**3 * getal2, 10**3 * (getal1 + getal2))
som5 = '{:6d} + {:<6d} = {}' .format(10**4 * getal1, 10**4 * getal2, 10**4 * (getal1 + getal2))

# uitvoer
print(som1)
print(som2)
print(som3)
print(som4)
print(som5)
