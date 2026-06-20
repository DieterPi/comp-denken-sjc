a = int(input("Geef een eerste getal in: "))
b = int(input("Geef een eerste getal in: "))
c = int(input("Geef een eerste getal in: "))
d = int(input("Geef een eerste getal in: "))

deler = 2
while a % deler != 0 or b % deler != 0 or c % deler != 0 or d % deler != 0:
    deler += 1
print()
print(f"De gemeenschappelijke deler is: {deler}")
