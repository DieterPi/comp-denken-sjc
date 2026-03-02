getal = int(input("Geef een eerste getal in: "))
max = -1
som = 0

while getal != -1:
    som += getal
    if getal > max:
        max = getal
    getal = int(input("Geef het volgende getal in: "))

totaal = (1 + max) * max // 2

if totaal == som:
    rest = max + 1
else:
    rest = totaal - som

print(f"Het getal {rest} ontbreekt.")
