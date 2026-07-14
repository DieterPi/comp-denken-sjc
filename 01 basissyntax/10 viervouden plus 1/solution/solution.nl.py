import math
getal = int(input("Geef een viervoud plus 1 in: "))

rangnummer = getal // 4
regel = math.ceil(math.sqrt(rangnummer + 1))
aantal_ervoor = (regel - 1) ** 2 - 1

print(f"{getal} staat op regel {regel} plaats {rangnummer - aantal_ervoor}")
