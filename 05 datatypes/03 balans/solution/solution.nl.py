def in_balans(testgewicht: int, gewichten: list) -> bool:
    flag = False
    
    for i in range(len(gewichten)):
        gewicht = gewichten[i]
        nodig = testgewicht - gewicht
        if nodig > 0:
            j = 0
            while j < len(gewichten) and not flag:
                if gewichten[j] == nodig and j != i:
                    flag = True
                j += 1
    return flag
