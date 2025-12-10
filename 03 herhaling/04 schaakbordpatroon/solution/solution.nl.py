r = int(input("Geef het aantal rijen: "))
c = int(input("Geef het aantal kolommen: "))

for i in range(r):
    aantal = c // 2
    if i % 2 == 0:
        print("X_" * aantal + "X" * max(0, c % 2))
    else:
        print("_X" * aantal + "_" * max(0, c % 2))
