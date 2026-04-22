getal = int(input("Geef een eerste getal in: "))

minimum = getal
som = 0
aantal = 0

while getal != -1:
    som += getal
    aantal += 1
    if getal < minimum:
        minimum = getal
    getal = int(input("Geef het volgende getal in: "))

aantal += 1
doel = (aantal + 1) * aantal // 2 + aantal * (minimum - 1)

rest = doel - som

print(f"Het getal {rest} ontbreekt.")
