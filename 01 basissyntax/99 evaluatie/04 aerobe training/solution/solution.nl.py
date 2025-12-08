licht = int(input("Geef het aantal minuten lichte intensiteit in: "))
hoog = int(input("Geef het aantal minuten lichte intensiteit in: "))

totaal = licht + 2 * hoog
verschil = 300 - totaal
print()
print("Je moet deze week nog:")
print(f"{verschil} minuten sporten aan lichte intensiteit of {round(verschil / 2)} minuten aan hoge intensiteit.")
