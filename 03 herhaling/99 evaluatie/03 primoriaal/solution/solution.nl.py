n = int(input("Geef een natuurlijk getal in: "))

primoriaal = 1
for getal in range(2, n + 1):
    
    aantal_delers = 0
    for i in range(1, getal):
        if getal % i == 0:
            aantal_delers += 1
            
    if aantal_delers == 1:
        primoriaal *= getal

print("De primoriaal van", n, "is", primoriaal)
