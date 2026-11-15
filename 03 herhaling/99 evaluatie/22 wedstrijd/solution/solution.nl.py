hoogste = 0
deelnemer = 0
for i in range(5):
    som = 0
    for j in range(4):
        score = int(input("Geef het de score in: "))
        som += score
    
    if som > hoogste:
        hoogste = som
        deelnemer = i

print(f"Deelnemer {deelnemer + 1} behaalde de hoogste score, namelijk: {hoogste} punten.")
