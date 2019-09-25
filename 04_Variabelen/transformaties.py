# invoer
a = int(input('met welk getal ga je de grafiek horizontaal verschuiven : '))
b = int(input('met welk getal ga je de grafiek verticaal verschuiven : '))
Fx = 'f(x) = 2(x - 3)^2 + 4'
t = a + 3
r = 4 + b

# berekening
Gx = 'g(x) = 2(x - ' + str(t) + ')^2 + ' + str(r)

# uitvoer
print(Fx)
print(Gx)
