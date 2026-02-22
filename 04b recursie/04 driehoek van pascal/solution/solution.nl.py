def pascal(rij, kolom):
    if rij == 0 or kolom == 0 or kolom == rij:
        return 1
    else:
        return pascal(rij - 1, kolom) + pascal(rij - 1, kolom - 1)
