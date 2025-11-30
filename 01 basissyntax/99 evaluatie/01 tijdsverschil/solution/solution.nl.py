uur1 = int(input("Geef het aantal uur van tijdstip 1 in: "))
minuut1 = int(input("Geef het aantal minuten van tijdstip 1 in: "))
uur2 = int(input("Geef het aantal uur van tijdstip 2 in: "))
minuut2 = int(input("Geef het aantal minuten van tijdstip 2 in: "))

minuten1 = uur1 * 60 + minuut1
minuten2 = uur2 * 60 + minuut2

verschil = minuten2 - minuten1

uur = verschil // 60
rest = verschil % 60

print(f"Verstreken tijd: {uur} uur en {rest} minuten.")
