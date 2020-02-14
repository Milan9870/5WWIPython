def roteer(woord, aantal):
    while aantal > len(woord):
      aantal -= len(woord)
    uitkomst = ''
    i = aantal
    while i + 1 != aantal:
        if i > len(woord):
            i -= len(woord)
        uitkomst += woord[i]
        i += 1

    return uitkomst


print(roteer('asimov', 3))
