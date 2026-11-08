getal = int(input("Geef een getal van drie cijfers in: "))

H = getal // 100
T = (getal // 10) % 10
E = getal % 10

if T < E:                 # laatste twee cijfers wisselen volstaat
    result = H * 100 + E * 10 + T
elif H < E:               # H < E <= T: E vooraan, rest oplopend
    result = E * 100 + H * 10 + T
elif H < T:               # E <= H < T: T vooraan, rest oplopend
    result = T * 100 + E * 10 + H
else:                     # cijfers dalend: geen groter getal mogelijk
    result = 0

if result == 0:
    print("Er is geen oplossing voor dit getal.")
else:
    print(result)