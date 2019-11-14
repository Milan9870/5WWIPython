# invoer
temperatuur = float(input('Geef de temperatuur: '))
lichtsterkte = float(input('Geef de lichtsterkte: '))

# berekenen
if lichtsterkte >= 10000:
    klasse = 'superreuzen (a)'
elif lichtsterkte >= 1000:
    klasse = 'superreuzen (b)'
elif lichtsterkte >= 100 and temperatuur < 7500:
    klasse = 'heldere reuzen'
elif lichtsterkte >= 10 and temperatuur < 6000:
    klasse = 'reuzen'
elif (lichtsterkte < 0.01 and temperatuur >= 5000) or (lichtsterkte < 0.0001 and temperatuur >= 3000):
    klasse = 'witte dwergen'
else:
    klasse = 'hoofdreeks'

# uitvoer
print(klasse)
