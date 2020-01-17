def is_grote_letter(t):
    return ord('A') <= ord(t) <= ord('Z')


def is_kleine_letter(t):
    return ord('a') <= ord(t) <= ord('z')


def is_letter(t):
    return is_kleine_letter(t) or is_grote_letter(t)


def roteer_letter(letter, cijfer):
    nieuwe_letter = ord(letter) + cijfer
    if od


print(roteer_letter('g', 20))


