getal = int(input("Geef een natuurlijk getal groter dan 1 in: "))
orig = getal

nio = 1

priem = 2
while getal != 1:
    if getal % priem == 0:
        nio *= (priem + 1)
        getal //= priem
    else:
        priem += 1

print("Het NIO-getal van", orig, "is:", nio)
