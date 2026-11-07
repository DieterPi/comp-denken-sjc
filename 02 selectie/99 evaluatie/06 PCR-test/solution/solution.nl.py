waarde = float(input("Geef de Ct-waarde in: "))

if waarde <= 13.1:
    sterkte = 'zeer sterk positief (superverspreider)'
elif waarde <= 19.5:
    sterkte = 'sterk positief'
elif waarde <= 26.0:
    sterkte = 'gewoon positief'
else:
    sterkte = 'zwak positief'

print(f"Deze persoon is {sterkte} besmet.")
