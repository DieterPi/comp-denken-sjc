bedrag = float(input("Geef het aankoopbedrag: "))
jaar = int(input("Geef het aantal levensjaren: "))

i = 0
while bedrag >= 1:
    i += 1
    minwaarde = bedrag * 2 / jaar
    bedrag -= minwaarde
    
    print(f"Na het {i} e jaar is de minwaarde: € {round(minwaarde, 2)}")
    
if i == 1:
    print(f"Na één jaar is het product quasi waardeloos geworden.")
else:
    print(f"Na {i} jaren is het product quasi waardeloos geworden.")
