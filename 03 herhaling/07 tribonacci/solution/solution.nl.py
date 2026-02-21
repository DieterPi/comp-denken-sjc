n = int(input("Geef het rangnummer in: ")) 

if n < 2: 
    nieuw = 0
elif n == 2:
    nieuw = 1
else: 
    a = 0
    b = 0
    c = 1
    for _ in range(n - 2): 
        nieuw = a + b + c
        a = b
        b = c
        c = nieuw

print(f"Het getal uit de rij van Tribonacci met rangnummer {n} is {nieuw}")
