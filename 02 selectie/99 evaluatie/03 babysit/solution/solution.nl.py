import math

startuur = int(input("Geef het startuur in: "))
startmin = int(input("Geef de startminuten in: "))
einduur = int(input("Geef het einduur in: "))
eindmin = int(input("Geef de eindminuten in: "))

# Tijd berekenen
minuten = einduur * 60 + eindmin - startuur * 60 - startmin
uren = math.ceil(minuten / 60)

bedrag = uren * 6
if bedrag < 10:
    bedrag = 10

if einduur >= 22:
    bedrag += 30

print(f"Vergoeding: € {bedrag}")
