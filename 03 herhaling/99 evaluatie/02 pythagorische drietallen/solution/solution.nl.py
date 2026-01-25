eindgetal = int(input("Geef een eindgetal in: "))

print(f"De pythagorese drietallen kleiner dan {eindgetal} zijn:")
for a in range(2, eindgetal):
    for b in range(2, a):
        for c in range(2 , b):
            if a**2 == b**2 + c**2:
                print(f"{a} , {b}, {c}")
