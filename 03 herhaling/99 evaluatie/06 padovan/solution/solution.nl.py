n = int(input("Geef het rangnummer in: ")) 
print()
if n <= 3: 
    print(f"Het {n}e getal is 1")
else: 
    a = 1 
    b = 1 
    c = 1
    for i in range(3, n + 1): 
        nieuw = a + b
        a = b
        b = c
        c = nieuw
        
    print(f"Het {n}e getal is {nieuw}")
