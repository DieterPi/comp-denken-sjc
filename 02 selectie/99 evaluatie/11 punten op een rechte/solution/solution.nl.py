a1 = int(input("Geef de eerste afstand: "))
a2 = int(input("Geef de tweede afstand: "))
a3 = int(input("Geef de derde afstand: "))

collineair = (a1 + a2 == a3 or a1 + a3 == a2 or a2 + a3 == a1)

if collineair:
    print("A, B en C liggen op eenzelfde rechte.")
else:
    print("A, B en C liggen niet op eenzelfde rechte.")
