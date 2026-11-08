volume = float(input("Geef het volume in cℓ: "))
massa = float(input("Geef de massa in g: "))

dichtheid = (massa / 1000) / (volume / 100)

if dichtheid > 1:
    status = "zinkt"
else:
    status = "drijft"

print(f"Deze vloeistof {status} in water.")
