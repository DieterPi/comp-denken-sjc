piek = int(input("Geef het jaarlijkse verbruik tijdens piekuren in: "))
dal = int(input("Geef het jaarlijkse verbruik tijdens daluren in: "))

easy = round(69 + 16.257 / 100 * piek + 13.150 / 100 * dal, 2)
empower = round(85 + 15.938 / 100 * piek + 11.186 / 100 * dal, 2)

if easy <= empower:
    print("EASY Vast is de goedkoopste formule")
    goedkoopst = easy
else:
    print("EMPOWER Vast is de goedkoopste formule")
    goedkoopst = empower

print(f"Jaarlijkse kostprijs: € {goedkoopst}")
