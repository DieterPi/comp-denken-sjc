aantal = int(input("Geef het aantal levens in: "))

for i in range(aantal):
    if aantal - i != 1:
        print(f"Nog {aantal - i} levens")
    else:
        print(f"Nog 1 leven")

print("Game Over")
