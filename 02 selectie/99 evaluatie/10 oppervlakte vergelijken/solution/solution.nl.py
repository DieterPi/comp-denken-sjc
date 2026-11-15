x = float(input("Geef de waarde van x in: "))
rechthoek = 2*x**2
vierkant = (x + 1)**2

if vierkant >= rechthoek:
    beste = "Het vierkant"
    opp = vierkant
else:
    beste = "De rechthoek"
    opp = rechthoek

print(f"{beste} heeft de grootste oppervlakte.")
print(f"Deze oppervlakte bedraagt: {round(opp, 2)}")
