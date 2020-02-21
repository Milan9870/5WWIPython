def hoogtemeters(lijst):
    verschil = []
    for i in range(0, len(lijst)-1):
        verschil.append(lijst[i + 1] - lijst[i])

    return verschil


def dalen_en_stijgen(verschil):
    dalen = 0
    stijgen = 0
    for i in verschil:
        if i < 0:
            dalen += -i
        else:
            stijgen += i

    return (dalen, stijgen)


