def volgende_getal(getal: int) -> int:
    getal_str = str(getal)
    
    count = 1
    prev = getal_str[0]
    nieuw = ""
    for i in range(1, len(getal_str)):
        char = getal_str[i]
        if char != prev:
            nieuw += str(count) + prev
            count = 1
            prev = char 
        else:
            count += 1
    
    nieuw += str(count) + prev
    
    return int(nieuw)

def speciale_rij(n: int) -> int:
    getal = 1
    for i in range(1,n):
        getal = volgende_getal(getal)
    
    return getal
