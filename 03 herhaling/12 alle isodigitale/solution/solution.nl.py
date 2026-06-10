bovengrens = int(input("Geef een bovengrens (< 1000) in: "))

print()
aantal = 0
for getal in range(100, bovengrens):
    H = getal // 100
    T = (getal % 100) // 10
    E = getal % 10
    
    if H != T and H != E and T != E:
        print(f"{getal} is niet-isodigitaal")
        aantal += 1

if aantal == 0:
    print(f"Er waren geen niet-isodigitale getallen kleiner dan {bovengrens}")
elif aantal == 1:
    print(f"Er was één niet-isodigitaal getal kleiner dan {bovengrens}")
else:
    print(f"Er waren {aantal} niet-isodigitale getallen kleiner dan {bovengrens}")
