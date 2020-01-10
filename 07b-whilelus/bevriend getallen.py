getal1 = int(input('Geef een getal: '))
getal2 = int(input('Geef een getal: '))
som_getal1 = 0
som_getal2 = 0

for i in range(1, getal1):
    if getal1 % i == 0:
        som_getal1 += i

for f in range(1, getal2):
    if getal2 % f == 0:
        som_getal2 += f

if som_getal1 == getal2 and som_getal2 == getal1:
    print(str(getal1) + ' en ' + str(getal2) + ' zijn bevriende getallen')
else:
    print(str(getal1) + ' en ' + str(getal2) + ' zijn geen bevriende getallen')
