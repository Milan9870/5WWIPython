# invoer
R = 2
fc = 0.2
il = float(input('Geef de waarde van il : '))
fi = float(input('Geef de waarde van fi : '))
L = float(input('Geef de waarde van L : '))

# berekening
N = R * fc * il * fi * L
N = int(N)


# uitvoer
print('samenlevingen in de melkweg waarmee we zouden kunnen communiceren: ' + str(N))
