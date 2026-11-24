aantal = int(input("Geef het aantal ritten in:"))

aantal22 = aantal // 10
aantal3 = aantal % 10
if aantal3 > 7:
    aantal3 = 0
    aantal22 = aantal22 + 1

totaal = aantal22 * 22 + aantal3 * 3

print(f"Totale kostprijs: € {totaal}")
print(f"Hierbij koop je {aantal3} keer een ticket van € 3 en {aantal22} keer een ticket van € 22.")
