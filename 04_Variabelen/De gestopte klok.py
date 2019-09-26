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
h5 = h4 - h1
m5 = m4 - m1
h6 = h3 - h2
m6 = m3 - m2
h7 = h5 - h6
m7 = m5 - m6
h8 = h7 / 2
m8 = m7 / 2
h9 = h8 + h3
m9 = m8 + m3

# uitvoer
print(int(h9))
print(int(m9))
