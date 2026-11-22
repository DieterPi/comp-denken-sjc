aantal = int(input("Geef het aantal ritten in:"))

aantal22 = aantal // 7
aantal3 = aantal - aantal22 * 10
if aantal3 < 0:
    aantal3 = 0

totaal = aantal22 * 22 + aantal3 * 3

print(f"Totale kostprijs: € {totaal}")
print(f"Hierbij koop je {aantal3} keer een ticket van € 3 en {aantal22} keer een ticket van € 22.")
