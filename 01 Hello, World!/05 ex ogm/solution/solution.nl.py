getal1 = int( input( 'Geef een getal van 3 cijfers in: ' ) )
getal2 = int( input( 'Geef een getal van 4 cijfers in: ' ) )
getal3 = int( input( 'Geef een getal van 3 cijfers in: ' ) )

output = (getal1 * 10000 * 1000 + getal2 * 1000 + getal3) % 97
print( 'controlegetal:', output )