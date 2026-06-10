getal = int(input("Geef een getal van 3 cijfers in: "))

H = getal // 100
T = (getal % 100) // 10
E = getal % 10

label = ""
if H != E and H != T and E != T:
    label = "niet "

print(f"{getal} is {label}isodigitaal.")
