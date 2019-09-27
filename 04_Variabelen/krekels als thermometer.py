# invoer
N60 = int(input('Hoeveel tjirps neem je waar per minuut : '))

# berekening
Tf = 50 + ((N60 - 40) / 4)
Tc = 10 + ((N60 - 40) / 7)

# uitvoer
print('temperatuur (Fahrenheit): ' + str(Tf))
print('temperatuur (Celsius): ' + str(Tc))
