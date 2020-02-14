from math import sqrt


def binnen_of_buiten(middelpunt, punt_op, punt):

    afstand = sqrt((middelpunt[0] - punt[0]) ** 2 + (middelpunt[1] - punt[1]) ** 2)
    straal = sqrt((middelpunt[0] - punt_op[0]) ** 2 + (middelpunt[1] - punt_op[1]) ** 2)

    if afstand > straal:
        uitkomst = 'buiten'
    elif afstand == straal:
        uitkomst = 'op'
    else:
        uitkomst = 'binnen'

    return uitkomst, round(afstand, 4)




