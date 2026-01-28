n = int(input("Geef het aantal in te voeren getallen in: "))

max = int(input("Geef een getal in: "))
min = max
for _ in range(n - 1):
    getal = int(input("Geef een getal in: "))
    if getal > max:
        max = getal
    if getal < min:
        min = getal

range = max - min

print(f"De variatiebreedte is {range}")
