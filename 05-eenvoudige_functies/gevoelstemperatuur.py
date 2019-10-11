# invoer
temperatuur = float(input('Wat is de luchttemperatuur in graden Celsius : '))
windsnelheid = float(input('Wat is de windsnelheid in meter per seconden : '))

# berekening
gevoelstemperatuur = 13.12 + (0.6215 * temperatuur) + ((0.3965 * temperatuur) - 11.37) * windsnelheid ** 0.16

# uitvoer
print(gevoelstemperatuur)
