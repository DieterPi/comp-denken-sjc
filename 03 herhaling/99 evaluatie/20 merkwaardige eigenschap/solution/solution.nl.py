for getal in range(10, 100):
    tiental = getal // 10
    eenheid = getal % 10
     
    totaal = tiental * eenheid + tiental + eenheid
    if totaal == getal:
        print(f"Het getal {getal} heeft deze bijzondere eigenschap.")
