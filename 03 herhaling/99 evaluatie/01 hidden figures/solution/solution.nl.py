n = int(input("Geef het eindgetal in: "))

print(1)
for getal in range(2, n + 1):
    delers = 0
    for i in range(1, getal):
        if getal % i == 0:
            delers += 1
    
    if delers == 1:
        print("priemgetal")
    else:
        print(getal)
