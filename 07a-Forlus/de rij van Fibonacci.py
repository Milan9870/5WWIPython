# invoer
n = int(input('hoeveelste getal in de rij van Fibonacci: '))
f1 = 1
f2 = 1

# berekening
for i in range(1, n - 1):
    som = f1 + f2
    f1 = f2
    f2 = som

# uitvoer
print(f2)
