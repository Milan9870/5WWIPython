# invoer
antwrd_1 = str(input('Trek je aan de hendel: '))
antwrd_2 = str(input('Duw je de man van de brug: '))

# berekenen
if antwrd_1 != antwrd_2:
    doden = '1'
elif antwrd_1 == 'ja':
    doden = '2'
else:
    doden = '5'


# uitvoer
print(doden)
