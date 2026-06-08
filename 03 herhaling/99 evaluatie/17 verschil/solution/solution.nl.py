import random

score = 0
for _ in range(5):
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    print(f"De getallen zijn: {a} en {b}")
    
    # Vraag de gebruiker naar het kwadraat van het getal
    antwoord = int(input("Bepaal het verschil van het grootste en kleinste getal: "))
    verschil = abs(a-b)
    if antwoord == verschil:
        print("Excellent! Dit levert een extra punt op.")
        score += 1
    else:
        print(f"Jandoedel, je verliest een punt! Het correcte antwoord was {verschil}")
        score -= 1

# Print de totaalscore van de gebruiker
if score == 1:
    print("Je behaalde één punt.")
else:
    print(f"Je behaalde {score} punten.")
