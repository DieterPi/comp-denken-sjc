getal = int(input("Geef het startgetal in: "))

print()
print("Startgetal:", getal)

i = 1
while getal != 495:
    H = getal // 100
    T = (getal // 10) % 10
    E = getal % 10
    
    grootst = max(H, T, E)
    kleinst = min(H, T, E)
    mid = H + T + E - grootst - kleinst
    
    getal1 = grootst * 100 + mid * 10 + kleinst
    getal2 = kleinst * 100 + mid * 10 + grootst
    
    getal = getal1 - getal2
    print(f"Na stap {i}: {getal}")
    i += 1
