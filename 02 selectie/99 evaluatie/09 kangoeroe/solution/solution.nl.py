a = int(input("Geef de positie van de eerste kangoeroe in: "))
b = int(input("Geef de positie van de tweede kangoeroe in: "))
c = int(input("Geef de positie van de derde kangoeroe in: "))

sprongen = max(b - a, c - b) - 1

if sprongen == 1:
    print("Er is één sprong mogelijk.")
else:
    print(f"Er zijn {sprongen} sprongen mogelijk.")
