import math
getal = int(input("Geef een natuurlijk getal in: "))
n = int(input("Geef het aantal iteraties in: "))

approx = math.floor(math.sqrt(getal))
r = getal - approx**2

add = 0
for _ in range(n):
    add = r / (2 * approx + add)

print(f"De benadering met {n} kettingbreuken is {round(approx + add, 6)}")
