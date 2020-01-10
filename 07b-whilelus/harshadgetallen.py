harshad = str(input('een getal: '))
deeltal = int(harshad)
som = 0

for cijfer in harshad:
    som += int(cijfer)

if deeltal % som == 0:
    print(str(deeltal) + ' is een Harshadgetal')
else:
    print(str(deeltal) + ' is geen Harshadgetal')

