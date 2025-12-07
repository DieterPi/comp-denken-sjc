diameter = int(input("Geef de diameter van de nieuwe pizza in: "))

nieuw = (diameter / 30) ** 2 * 11

print(f"Een pizza met diameter {diameter} cm heeft als kostprijs € {round(nieuw, 2)}")
