aantal = int(input("Geef het aantal snoepjes in: "))
euro = int(input("Geef het aantal euro's in: "))
cent = int(input("Geef het aantal cent in: "))

totaal_cent = cent * aantal
totaal_euro = euro * aantal + totaal_cent // 100

print("Totale prijs:", totaal_euro, "euro", totaal_cent % 100, "eurocent.")
