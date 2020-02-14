def verwijder_medeklinkers(woord):
    uitkomst = ''
    i = 0
    if woord[0] in ' zrtypqsdfghjklmwxcbn':
        for i in range(0, len(woord)):
            if woord[i] in 'aeuio':
                for t in range(i, len(woord)):
                    uitkomst += woord[t]
                i += len(woord)
    else:
        uitkomst = woord

    return uitkomst


def varkenslatijn(woord):
    if woord[0] in ' zrtypqsdfghjklmwxcbn':
        if woord[len(woord)] in 'aeuio':
            verwijder_medeklinkers(woord)
            woord += 'nt'
        else:
            verwijder_medeklinkers(woord)
            woord += 'itum'
    else:
        woord += 'ibum'
    woord.replace('j', 'i')
    woord.replace('y', '')
    woord.replace('z', '')


def vertaal(zin):
    uitkomst = ''
    for i in range(0, len(zin)):
        woord = ''
        while zin[i+1] != ' ':
            woord += zin[i]
            i += 1
        uitkomst += varkenslatijn(woord)

    return uitkomst




