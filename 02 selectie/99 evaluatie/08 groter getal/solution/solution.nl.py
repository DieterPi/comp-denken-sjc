getal = int(input("Geef een getal van drie cijfers in: "))

H = getal // 100
T = (getal // 10) % 10
E = getal % 10

if T < E:
    result = H * 100 + E * 10 + T
elif H < T: # en T >= E
    if E < H:
        result = T * 100 + E * 10 + H
    else:
        result = T * 100 + H * 10 + E
else:
    result = 0

if result == 0:
    print("Er is geen oplossing voor dit getal.")
else:
    print(result)