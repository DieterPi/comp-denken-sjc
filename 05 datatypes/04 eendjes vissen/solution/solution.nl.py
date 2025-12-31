def bepaal_nummer(eendjes: list) -> int:
    n = len(eendjes)
    som = 0
    index = 0
    for i in range(n - 4):
        nieuw = eendjes[i] + eendjes[i + 1] + eendjes[i + 2] + eendjes[i + 3]
        if nieuw > som:
            som = nieuw
            index = i
    
    return index + 1
