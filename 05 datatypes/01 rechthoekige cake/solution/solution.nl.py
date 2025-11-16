def lengte_cake(breedte: int, stukken: list) -> int:
    opp = 0
    for stuk in stukken:
        opp += stuk[0] * stuk[1]
    
    lengte = opp // breedte
    
    return round(lengte, 2)
