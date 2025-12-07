import math

r = float(input( 'Geef de straal van de bol in (in cm): ' ))

oppervlakte = round(4 * math.pi * r ** 2, 2)
volume = round(4 / 3 * math.pi * r ** 3, 2)

print()
print(f"oppervlakte: {oppervlakte} cm²")
print(f"volume: {volume} cm³")
