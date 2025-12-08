uur = int(input('Geef het aantal uur in: '))
minuut = int(input('Geef het aantal minuten in: '))
seconde = int(input('Geef het aantal seconden in: '))

hoek = uur * 30 + minuut * 30 / 60 + seconde * 30 / ( 60 * 60 )

print(f"{round(hoek, 5)} graden")
