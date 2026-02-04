a = int(input("Geef het eerste getal in: "))
b = int(input("Geef het eerste getal in: "))

som1 = 0
for i in range(1, a):
    if a % i == 0:
        som1 += i

som2 = 0
for i in range(1, b):
    if b % i == 0:
        som2 += i

if som1 == b and a == som2:
    status = "bevriend"
else:
    status = "niet bevriend"

print(a, "en", b, "zijn", status + ".")
