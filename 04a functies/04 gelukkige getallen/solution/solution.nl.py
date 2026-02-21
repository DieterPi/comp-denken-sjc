def som_kwadraten(getal: int) -> int:
    som = 0
    while getal > 0:
        som += (getal % 10) ** 2
        getal //= 10
    
    return som

def is_gelukkig(getal: int) -> bool:
    gezien = {getal}
    while getal != 1:
        getal = som_kwadraten(getal)
        if getal in gezien:
            return False
        else:
            gezien.add(getal)
    return True

getal = int(input("Geef een natuurlijk getal in: "))

if is_gelukkig(getal):
    print(f"{getal} is een gelukkig getal.")
else:
    print(f"{getal} is geen gelukkig getal.")
