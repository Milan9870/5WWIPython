# invoer
s = int(input('Geef een geheel aantal seconden : '))

# berekening
m = s // 60
s = s % 60
u = m // 60
m = m % 60
d = u // 24
u = u % 24

# uivoer
print(str(d) + 'd ' + str(u) + ':' + str(m) + ':' + str(s))
