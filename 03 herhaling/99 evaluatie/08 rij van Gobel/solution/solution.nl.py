n = int(input("Geef het rangnummer in: "))

if n <= 2:
    getal = 1
else:
    a = 1
    b = 1
    som_kwadraten = a**2 + b**2
    for i in range(n - 2):
        getal = som_kwadraten // (i + 1)
        a = b
        b = getal
        som_kwadraten += getal**2

print(f"Het {n}e getal is {getal}")
