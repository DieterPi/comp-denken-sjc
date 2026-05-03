getal = int(input("Geef een getal in: "))
minimum = getal
maximum = getal

while getal != -1:
    if getal < minimum:
        minimum = getal
    if getal > maximum:
        maximum = getal
    getal = int(input("Geef een getal in: "))

variatiebreedte = maximum - minimum
print(f"De variatiebreedte is {variatiebreedte}")
