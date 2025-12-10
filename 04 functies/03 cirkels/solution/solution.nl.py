import math

def afstand(x1: float, y1: float, x2: float, y2: float) -> float:
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def onderlinge_ligging(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float) -> str:
    d = afstand(x1, y1, x2, y2)
        
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            ligging = "samenvallend"
        else:
            ligging = "concentrisch"
    else:
        # laat het eerste punt de grootste cirkel zijn
        if r2 > r1:
            x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1
            
        if d == r2 + r1:
            ligging = "uitwendig rakend"
        elif d == r2 - r1:
            ligging = "inwendig rakend"
        elif d < r2 + r1:
            ligging = "snijdend"
        elif d > r2 + r1:
            ligging = "uitwendig disjunct"
        else:
            ligging = "inwendig disjunct"       
    
    return ligging
