# invoer
h1 = int(input('geef het uur dat Andrea vertrekt van haar huis : '))
m1 = int(input('geef het aantal minuten na het uur dat Andrea vertrekt van haar huis : '))
h2 = int(input('geef het uur dat Andrea aankomt bij haar vriendin : '))
m2 = int(input('geef het aantal minuten na het uur uur dat Andrea aankomt bij haar vriendin : '))
h3 = int(input('geef het uur dat Andrea vertrekt bij haar vriendin : '))
m3 = int(input('geef het aantal minuten na het uur dat Andrea vertrekt bij haar vriendin : '))
h4 = int(input('geef het uur dat Andrea terug thuis komt : '))
m4 = int(input('geef het aantal minuten na het uur dat Andrea terug thuis komt : '))

# berekening
h1 = h1 * 60
h2 = h2 * 60
h3 = h3 * 60
h4 = h4 * 60
y1 = h1 + m1
y2 = h2 + m2
y3 = h3 + m3
y4 = h4 + m4

y5 = abs(y4 - y1)
y6 = abs(y3 - y2)
y7 = abs(y5 - y6)
y8 = y3 + y7

h8 = y8 // 60
m8 = y8 % 60

# uitvoer
print(int(h8))
print(int(m8))
