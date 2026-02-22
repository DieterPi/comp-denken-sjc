grens = int(input("Geef de bovengrens in: "))

benadering = 1
aantal_factoren = 0
for getal in range(3, grens):
    
    aantal = 0
    for i in range(1, getal):
        if getal % i == 0:
            aantal += 1
    
    if aantal == 1:
        benadering *= (1 - 1 / (getal - 1)**2)
        aantal_factoren += 1

if aantal_factoren == 1:
    print(f"De benadering voor de tweelingsconstante met 1 factor bedraagt {round(benadering, 9)}")
else:
    print(f"De benadering voor de tweelingsconstante met {aantal_factoren} factoren bedraagt {round(benadering, 9)}")
