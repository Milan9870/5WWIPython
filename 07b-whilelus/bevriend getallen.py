getal_1 = int(input('Geef een getal: '))
getal_2 = int(input('Geef een getal: '))
som_getal_1 = 0
som_getal_2 = 0

for getal_3 in range(1, getal_1):
    if getal_1 % getal_3 == 0:
        som_getal_1 += getal_3

for getal_3 in range(1, getal_2):
    if getal_2 % getal_3 == 0:
        som_getal_2 += getal_3

if som_getal_1 == getal_2 and som_getal_2 == getal_1:
    print(str(getal_1) + ' en ' + str(getal_2) + ' zijn bevriende getallen')
else:
    print(str(getal_1) + ' en ' + str(getal_2) + ' zijn geen bevriende getallen')
