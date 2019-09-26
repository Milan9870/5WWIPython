# invoer
sol = int(input('geef een aantal marsdagen : '))

# berekening
dagen = sol
minuten = sol * 39
seconden = sol * 35.244
minutenn = seconden // 60
seconden = seconden % 60
minuten = minuten + minutenn
uurr = minuten // 60
minuten = minuten % 60
dagenn = uurr // 60
uur = uurr % 60
dagen = dagen + dagenn

# uitvoer
print(str(sol) + ' sol = ' + str(dagen) + ' dagen, ' + str(uur) + ' uur, ' + str(minuten) + ' minuten en ' + str(seconden) + ' seconden')
