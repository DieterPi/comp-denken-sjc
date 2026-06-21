zoon = int(input("Geef de leeftijd van de zoon in: "))
moeder = int(input("Geef de leeftijd van de moeder in: "))

i = 0
teller = 0
while zoon > 9:
    zoon_T = zoon // 10
    zoon_E = zoon % 10
    moeder_T = moeder // 10
    moeder_E = moeder % 10
    
    if zoon_T == moeder_E and zoon_E == moeder_T:
        teller += 1
        if i == 0:
            print(f"Dit jaar is de zoon {zoon} en de moeder {moeder} jaar.")
        else:
            print(f"{i} jaar geleden was de zoon {zoon} jaar en de moeder {moeder} jaar.")
    zoon -= 1
    moeder -= 1
    i += 1

if teller == 0:
    print("De leeftijden waren nooit elkaars omgekeerde.")
