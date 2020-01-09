woord = str(input('wat is het woord: '))
geldbedrag = int(input('Wat is het gedraaide geldbedrag: '))
letter = str(input('Geef een letter: '))
gewonnen_bedrag = 0
gegeven_letters = ''

while (letter in woord) and not (letter in gegeven_letters):
    gegeven_letters += letter
    gewonnen_bedrag += geldbedrag
    letter = str(input('Geef een letter: '))


print(gewonnen_bedrag)
