import math
getal = int(input("Geef een natuurlijk getal in (> 0): "))

rang = math.ceil(math.sqrt(getal))
aantal_rij = 2 * rang - 1
plaats = aantal_rij - (rang ** 2 - getal)

print(f"{getal} staat in regel {rang} op plaats {plaats}")
