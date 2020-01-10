tijdstip = int(input('geef een tijdstip: '))
stappen = 0
gezette_stappen = 0

for i in range(1, tijdstip + 1):
    if i % 2 != 0:
        gezette_stappen = gezette_stappen * 2 + 2
        stappen += gezette_stappen
    else:
        gezette_stappen /= 2
        stappen -= gezette_stappen

print(int(stappen))

