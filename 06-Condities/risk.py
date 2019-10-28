# invoer
aanvaller_1 = int(input('Eerste dobbelsteen aanvaller: '))
aanvaller_2 = int(input('Tweede dobbelsteen aanvaller: '))
aanvaller_3 = int(input('Derde dobbelsteen aanvaller: '))
verdediger_1 = int(input('Eerste dobbelsteen verdediger: '))
verdediger_2 = int(input('Tweede dobbelsteen verdediger: '))

# berekening
if max(aanvaller_1, aanvaller_2, aanvaller_3) > max(verdediger_1, verdediger_2):
    if aanvaller_1 + aanvaller_2 + aanvaller_3 - max(aanvaller_1, aanvaller_2, aanvaller_3) - min(aanvaller_1, aanvaller_2, aanvaller_3) > min(verdediger_1, verdediger_2):
        uitkomst = 'aanvaller verliest 0 legers, verdediger verliest 2 legers'
    else:
        uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
else:
    if aanvaller_1 + aanvaller_2 + aanvaller_3 - max(aanvaller_1, aanvaller_2, aanvaller_3) - min(aanvaller_1, aanvaller_2, aanvaller_3) > min(verdediger_1, verdediger_2):
        uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
    else:
        uitkomst = 'aanvaller verliest 2 legers, verdediger verliest 0 legers'

# uitvoer
print(uitkomst)
