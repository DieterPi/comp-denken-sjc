vader = int(input("Geef de leeftijd van de vader in: "))
vader += 1
dochter = 1

i = 0
while vader / dochter >= 2:
    if vader % dochter == 0:
        i += 1
        print(f"{i} e keer: dochter is {dochter} jaar en de vader is {vader} jaar")
    vader += 1
    dochter += 1
print(f"Dit kwam {i} keer voor.")
