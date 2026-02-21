def nio_nummer(getal: int) -> int:
    som = 0
    t = len(str(getal))
    while getal > 0:
        som += t * (getal % 10)
        getal = getal // 10
        t -= 1
        
    return som

def nio_limiet(getal: int) -> int:
    nieuw = nio_nummer(getal)
    while getal != nieuw:
        getal = nieuw
        nieuw = nio_nummer(getal)
    
    return getal
    