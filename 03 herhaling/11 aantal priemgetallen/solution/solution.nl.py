getal = int(input("Geef een getal in: "))
aantal_priem = 0
while getal != 0:   
    aantal_delers = 0
    i = 2
    while i < getal and aantal_delers == 0:
        if getal % i == 0:
            aantal_delers += 1
        i += 1
    
    if aantal_delers == 0 and getal >= 2:
        aantal_priem += 1
    getal = int(input("Geef een getal in: "))

if aantal_priem == 0:
    print("Er werden geen priemgetallen ingevoerd.")
elif aantal_priem == 1:
    print("Er werd één priemgetal ingevoerd.")
else:
    print(f"Er werden {aantal_priem} priemgetallen ingevoerd.")
