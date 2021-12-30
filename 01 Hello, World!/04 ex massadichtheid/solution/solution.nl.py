# vul de juiste invoer in
getal1 = int( input( 'Geef het eerste getal in: ' ) )
getal2 = int( input( 'Geef het tweede getal in: ' ) )
getal3 = int( input( 'Geef het derde getal in: ' ) )

# vul hieronder de andere uitvoer aan
print('maximum:', max( getal1, getal2, getal3 ) )
print('minimum:', min( getal1, getal2, getal3 ) )
print('gemiddelde:', round( ( getal1 + getal2 + getal3 ) / 3 , 2 ) )