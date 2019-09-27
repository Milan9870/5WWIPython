# invoer
t = int(input('Geef een aantal nanoseconden : '))
n = 1.000277
c = 299792458
t = t * 10**-9

# berekening
d = (c * t) / (2 * n)



# uitvoer
print(str(d) + ' meter')
