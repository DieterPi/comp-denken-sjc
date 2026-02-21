def digitale_som(getal):
    if getal < 10:
        return getal
    else:
        e = getal % 10
        return digitale_som(getal // 10 + e)
