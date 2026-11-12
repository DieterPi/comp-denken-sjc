import math
getal = int(input("Geef het getal in: "))

rang = math.floor( (math.sqrt(1+ 4 * 2 * getal) - 1) / 2 )
aantal_ervoor = rang * (rang + 1) // 2
kolom = getal - aantal_ervoor

print(f"{getal} staat op regel {rang} en kolom {kolom}")
