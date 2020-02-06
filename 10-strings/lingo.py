def hint(gegokte_woord, woord):
    hint = ''
    for i in range(0, len(gegokte_woord)):
        if gegokte_woord[i] not in woord:
            hint += '.'
        elif gegokte_woord[i] == woord[i]:
            hint += gegokte_woord[i].upper()
        else:
            hint += gegokte_woord[i]

    return hint


print(hint('hiust', 'vuolt'))
