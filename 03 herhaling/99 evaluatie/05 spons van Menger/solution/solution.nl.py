# Invoer vragen
z = float( input( "Geef de lengte van de ribbe in: " ) )
n = int( input( "Geef het volgnummer in: " ) )

# Berekeningen + uitvoer
print(f"De startkubus heeft een volume van {round(z**3, 4)} cm³.")
aantal = 1
for i in range(n):
    aantal *= 20
    z /= 3
    V = aantal * z**3
    print(f"Na stap {i + 1} zijn er {aantal} kubussen in het totaal en is het totale volume {round(V, 4)} cm³.")
