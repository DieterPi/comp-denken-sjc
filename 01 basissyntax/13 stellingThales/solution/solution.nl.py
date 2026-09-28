h = float(input("Hoe groot is het kleinere object? "))
l = float(input("Hoe lang is de schaduw ervan? "))
grote_l = float(input("Hoe lang is de schaduw van het grote object? "))

grote_h = grote_l * h / l
print()
print(f"Het grote object is ongeveer {round(grote_h, 2)} m hoog.")
