z = int(input("Geef de zijde in: "))
n = int(input("Geef een getal uit dit rooster in: "))

rij = (n - 1) // z
kolom = (n - 1) % z

print()
print(f"Rijnummer: {rij}")
print(f"Kolomnummer: {kolom}")
