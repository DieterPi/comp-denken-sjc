import math

lengte = float(input("Geef de lengte van de vloer in (in m): "))
breedte = float(input("Geef de breedte van de vloer in (in m): "))
zijde = float(input("Geef de zijde van een tegel in (in m): "))

aantal_lengte = math.ceil(lengte / zijde)
aantal_breedte = math.ceil(breedte / zijde)

aantal = aantal_breedte * aantal_lengte
print()
print(f"Aantal tegels in de lengte: {aantal_lengte}")
print(f"Aantal tegels in de breedte: {aantal_breedte}")
print(f"Er zijn dus minimaal {aantal} tegels nodig.")
