# invoer
getal = int(input('Geef een getal: '))
som = 0

# berekenen
for veelvoud in range(getal, 101, getal):
    som = veelvoud + som

print(som)
