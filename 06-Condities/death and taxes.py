# invoer
brutoloon = float(input('Geef een brutoloon: '))

# berekenen
rsz = brutoloon * 13.07 / 100
netto_belastbaar_inkomen = brutoloon - rsz
if netto_belastbaar_inkomen > 13250.00:
    schijf_1 = 13250.00 * 25 / 100
    netto_belastbaar_inkomen -= 13250.00
else:
    schijf_1 = netto_belastbaar_inkomen * 25 / 100
    netto_belastbaar_inkomen = 0
if netto_belastbaar_inkomen > 10140.00:
    schijf_2 = 10140.00 * 40 / 100
    netto_belastbaar_inkomen -= 10140.00
else:
    schijf_2 = netto_belastbaar_inkomen * 40 / 100
    netto_belastbaar_inkomen = 0
if netto_belastbaar_inkomen > 17090.00:
    schijf_3 = 17090.00 * 45 / 100
    netto_belastbaar_inkomen -= 17090.00
else:
    schijf_3 = netto_belastbaar_inkomen * 45 / 100
    netto_belastbaar_inkomen = 0

schijf_4 = netto_belastbaar_inkomen * 50 / 100

voorheffing = schijf_1 + schijf_2 + schijf_3 + schijf_4
netto_belastbaar_inkomen = brutoloon - rsz
netto_jaarsalaris = netto_belastbaar_inkomen - voorheffing
netto_maandsalaris = netto_jaarsalaris / 12

# uitvoer
print('+ bruto jaarsalaris' + '{:>13.2f}'.format(brutoloon))
print('- rsz' + '{:>27.2f}'.format(rsz))
print('- voorheffing' + '{:>19.2f}'.format(voorheffing))
print(32 * '=')
print('+ netto jaarsalaris' + '{:>13.2f}'.format(netto_jaarsalaris))
print('+ netto maandsalaris' + '{:>12.2f}'.format(netto_maandsalaris))


