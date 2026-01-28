n = int(input("Geef het aantal in te voeren getallen in: "))

max = int(input("Geef een getal in: "))
for _ in range(n - 1):
    getal = int(input("Geef een getal in: "))
    if getal > max:
        max = getal

print(f"Van de {n} ingevoerde getallen was {max} het grootste getal.")
