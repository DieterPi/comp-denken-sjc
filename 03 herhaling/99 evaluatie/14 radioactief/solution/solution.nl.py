massa = float(input("Geef de hoeveelheid radioactief afval: "))
i = 0

while massa >= 1:
    i += 1
    massa /= 2
    print(f"Na {i*30} resteert nog {round(massa, 1)} kg.")

if i == 0:
    print("Deze zone is al veilig.")
else:
    print(f"Na {i*30} jaar kan deze zone veilig verklaard worden.")
