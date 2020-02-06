def is_grote_letter(t):
    return ord('A') <= ord(t) <= ord('Z')


def is_kleine_letter(t):
    return ord('a') <= ord(t) <= ord('z')


def is_letter(t):
    return is_kleine_letter(t) or is_grote_letter(t)


def roteer_letter(letter, plaatsen):
    volgnummer_letter = min(ord(letter) % ord('a'), ord(letter) % ord('A'))
    nieuw_volgnummer = (volgnummer_letter + plaatsen) % 26
    offset = nieuw_volgnummer - volgnummer_letter
    return chr(ord(letter) + offset)


def versleutel(woord, n):
    rotatie = ''
    for letter in woord:
        rotatie += roteer_letter(letter, n)
    return rotatie


