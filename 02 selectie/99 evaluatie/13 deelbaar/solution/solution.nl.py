deeltal = int(input("Geef het deeltal in: "))
deler = int(input("Geef de deler in: "))

rest = deeltal % deler

if rest == 0:
    status = "deelbaar"
else:
    status = "niet deelbaar"

print(f"{deeltal} is {status} door {deler}")
