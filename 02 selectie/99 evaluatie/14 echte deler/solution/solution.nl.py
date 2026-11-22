deeltal = int(input("Geef het deeltal in: "))
deler = int(input("Geef de deler in: "))

rest = deeltal % deler

if rest == 0 and deler != 1 and deler != deeltal:
    status = "echte"
else:
    status = "geen echte"
print()
print(f"{deler} is {status} deler van {deeltal}")
