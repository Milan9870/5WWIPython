# invoer
speler1 = str(input('Blad, steen of schaar: '))
speler2 = str(input('Blad, steen of schaar: '))

# berekening
if speler1 == speler2:
    winnaar = 'onbeslist'
elif speler1 == 'blad':
    if speler2 == 'steen':
        winnaar = 'speler 1 wint'
    else:
        winnaar = 'speler 2 wint'
elif speler1 == 'steen':
    if speler2 == 'blad':
        winnaar = 'speler 2 wint'
    else:
        winnaar = 'speler 1 wint'
else:
    if speler2 == 'blad':
        winnaar = 'speler 1 wint'
    else:
        winnaar = 'speler 2 wint'


# uitvoer
print(winnaar)
# onbeslist en speler 1 wint programmeren, speler 2 wint in else
