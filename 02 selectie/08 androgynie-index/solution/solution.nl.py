import math
geslacht = input("Geef je geslacht in: (man/vrouw) ")
b = int(input("Geef de borstomtrek (in cm): "))
t = int(input("Geef de tailleomtrek (in cm): "))
h = int(input("Geef de heupomtrek (in cm): "))

index = round(t / math.sqrt(h * b), 2)

print(f"Androgynie-index: {index}")

if geslacht == "vrouw":
    if 0.67 < index < 0.70:
        print("Je komt in aanmerking als model")
    else:
        print("Je komt niet in aanmerking als model")
else:
    if 0.80 < index < 0.84:
        print("Je komt in aanmerking als model")
    else:
        print("Je komt niet in aanmerking als model")
