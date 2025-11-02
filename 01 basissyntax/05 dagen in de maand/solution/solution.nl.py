maandnummer = int(input("Geef het maandnummer in: "))

if (maandnummer % 2 != 0 and maandnummer <= 7) or maandnummer == 8 or maandnummer == 10 or maandnummer == 12:
    aantal_dagen = 31
elif maandnummer == 2:
    aantal_dagen = 28
else:
    aantal_dagen = 30

print("Maand", maandnummer, "bevat", aantal_dagen, "dagen.")
