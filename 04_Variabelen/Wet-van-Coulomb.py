# invoer
r = float(input('r: '))
r = r * 10E-2
q1 = 2.0E-6
q2 = 1.0E-6
k0 = 8.99E9

# berekening
fc = k0 * ((q1 * q2) / (r**2))

# uitvoer
print(fc)
