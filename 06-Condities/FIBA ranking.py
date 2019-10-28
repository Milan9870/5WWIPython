# invoer
thuisploeg = int(input('Hoeveel punten heeft de thuisploeg: '))
uitploeg = int(input('Hoeveel punten heeft de uitploeg: '))

# berekening
if abs(thuisploeg - uitploeg) < 10:
    if thuisploeg > uitploeg:
        puntenthuis = 530.00
        puntenuit = 470.00
    else:
        puntenthuis = 330.00
        puntenuit = 670.00
elif abs(thuisploeg - uitploeg) < 20:
    if thuisploeg < uitploeg:
        puntenthuis = 230.00
        puntenuit = 770.00
    else:
        puntenthuis = 630.00
        puntenuit = 370.00
else:
    if thuisploeg < uitploeg:
        puntenthuis = 130.00
        puntenuit = 870.00
    else:
        puntenthuis = 730.00
        puntenuit = 270.00

puntenthuis = '{:.2f}'.format(puntenthuis)
puntenuit = '{:.2f}'.format(puntenuit)

# uitvoer
print('thuisploeg: ' + str(puntenthuis))
print('uitploeg: ' + str(puntenuit))



