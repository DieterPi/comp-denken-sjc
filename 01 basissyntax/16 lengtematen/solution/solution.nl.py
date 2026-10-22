import math
lengte = float(input("Geef de lengte in m in: "))

inch = lengte * 100 / 2.54
yard = math.floor(inch / 36)
inch = inch - yard * 36
feet = math.floor(inch / 12)
inch = inch - feet * 12

print(f"Dit stemt overeen met {yard} yard {feet} feet {round(inch, 2)} inch")
