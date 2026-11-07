x1 = int(input("Geef de x-coördinaat van het eerste punt in: "))
y1 = int(input("Geef de y-coördinaat van het eerste punt in: "))
x2 = int(input("Geef de x-coördinaat van het tweede punt in: "))
y2 = int(input("Geef de y-coördinaat van het tweede punt in: "))

if x1 != x2:
    rico = round( ( y2 - y1 ) / ( x2 - x1 ), 2)
    print("De rico van de rechte door deze punten is", rico )
    if rico > 0:
        ligging = "stijgend"
    elif rico < 0:
        ligging = "dalend"
    else:
        ligging = "horizontaal"
    print(f"Deze rechte is {ligging}.")
else:
    print("Deze rechte heeft geen rico!")
