def ontdubbelen(woord):
    woord += ' '
    uitkomst = ''
    for i in range(0, len(woord)):
        if woord[i] != woord[i - 1]:
            uitkomst += woord[i]

    return uitkomst.strip()


