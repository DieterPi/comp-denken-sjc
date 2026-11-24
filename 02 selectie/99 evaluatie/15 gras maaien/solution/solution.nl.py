n = int(input("Geef het aantal rijen in: "))
m = int(input("Geef het aantal kolommen in: "))

if n < m:
    opt = 2 * (n - 1)
else:
    opt = 2 * (m - 1)

print(f"Mikro moet zijn grasmaaier {opt} keer draaien.")
