import math

lengte = float(input("Geef de lengte van de vloer in (in m): "))
breedte = float(input("Geef de breedte van de vloer in (in m): "))
zijde = float(input("Geef de zijde van een tegel in (in cm): "))

lengte *= 100
breedte *= 100

aantal_lengte = math.ceil(lengte / zijde)
aantal_breedte = math.ceil(breedte / zijde)

aantal = aantal_breedte * aantal_lengte

print()
print(f"Er zijn minimaal {aantal} tegels nodig.")
