kracht = float(input("Geef een kracht (in N) in: "))
uitrekking = int(input("Geef een uitrekking (in cm) in: "))

uitrekking /= 100

veerconstante = kracht / uitrekking

print(f"De veerconstante bedraagt {round(veerconstante, 2)} N/m.")
