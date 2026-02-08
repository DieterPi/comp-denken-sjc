n = int(input("Geef het eindgetal in: "))

som = 0
aantal_termen = 0
for getal in range(2, n + 1):
    aantal_delers = 0
    for i in range(2, getal):
        if getal % i == 0:
            aantal_delers += 1
        
    if aantal_delers == 0:
        som += 1 / getal
        aantal_termen += 1

print(f"De divergente som met {aantal_termen} termen is {round(som,6)}")
