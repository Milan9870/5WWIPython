# invoer
getal1 = float(input('geef een willekeurig getal : '))
getal2 = float(input('geef een tweede willekeurig getal : '))

# berekenen
rechterlid = abs(abs(getal1)-abs(getal2))
linkerlid = abs(getal1 - getal2)
rechterlid = round(rechterlid, 4)
linkerlid = round(linkerlid, 4)

# uitvoer
print(str(rechterlid) + ' \N{LESS-THAN OR EQUAL TO} ' + str(linkerlid))
