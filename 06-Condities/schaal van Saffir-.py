windsnelheid = int(input('Wat is de windsnelheid: '))

if windsnelheid >= 250:
    categorie = 'categorie 5'
elif windsnelheid >= 210:
    categorie = 'categorie 4'
elif windsnelheid >= 178:
    categorie = 'categorie 3'
elif windsnelheid >= 154:
    categorie = 'categorie 2'
elif windsnelheid >= 119:
    categorie = 'categorie 1'
else: categorie = 'geen orkaan'

print(categorie)
