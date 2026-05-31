getal = int(input("Geef het startgetal: "))
kopie = getal
n = 1

while getal != 1:
    if getal % 2 == 0:
        getal = getal // 2
    else:
        getal = 3 * getal + 1
    n += 1

print(f"De Collatzlengte van {kopie} is {n}")
