PI = 3.141592
straal = float(input( 'Geef de straal van de bol in (in cm): ' ))

oppervlakte = 4*PI*pow(straal, 2)
volume = 4/3*PI*pow(straal, 3)

print( 'oppervlakte:', round( oppervlakte, 2 ), 'cm²')
print( 'volume:', round( volume, 2 ), 'cm³')