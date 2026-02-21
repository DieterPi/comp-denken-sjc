getal1 = int(input("Geef een eerste getal in: "))
getal2 = int(input("Geef een tweede getal in: "))

a = max( getal1, getal2 )
b = min( getal1, getal2 )
rest = a % b

while rest != 0:
    a = b
    b = rest
    rest = a % b

print(f"De grootste gemene deler van {getal1} en {getal2} is {b}")
