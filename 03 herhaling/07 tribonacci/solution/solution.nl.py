n = int(input("Geef het rangnummer in: ")) 

if n <= 2: 
    nieuw = 0
elif n == 3:
    nieuw = 1
else: 
    a = 0
    b = 0
    c = 1
    for _ in range(n - 3): 
        nieuw = a + b + c
        a = b
        b = c
        c = nieuw

print(f"Het {n}e getal is {nieuw}")
