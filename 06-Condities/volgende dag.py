# invoer
dag = int(input('Geef de dag van vandaag: '))
maand = int(input('Geef de maand: '))
jaar = int(input('Geef het jaar: '))

# berekenen
volgende_dag = dag + 1
if maand % 2 == 1 and volgende_dag > 31 and maand <= 7:
    maand += 1
    volgende_dag = 1
elif maand % 2 == 0 and volgende_dag > 31 and maand > 7:
    maand += 1
    volgende_dag = 1
elif maand % 2 == 1 and volgende_dag > 30 and maand > 7 and maand != 12:
    maand += 1
    volgende_dag = 1
elif maand % 2 == 1 and volgende_dag > 31 and maand <=7 and maand != 2:
    maand += 1
    volgende_dag = 1
elif maand == 12 and volgende_dag > 31:
    jaar += 1
    maand = 1
    volgende_dag = 1
elif maand == 2:
    if(jaar % 100 != 0 and jaar % 400 == 0) and volgende_dag > 28:
        maand += 1
        volgende_dag = 1
    elif jaar % 4 == 0 and volgende_dag > 28:
        maand += 1
        volgende_dag = 1
    else:
        if volgende_dag > 29:
            maand += 1
            volgende_dag = 1

# uitvoer
print(str(volgende_dag) + '/' + str(maand) + '/' + str(jaar))


