bovengrens = int(input("Geef een bovengrens in: "))

som = 0
for i in range(3, bovengrens):
    if i % 5 == 0 or i % 3 == 0:
        som += i

print(f"De som van de veelvouden is {som}")
