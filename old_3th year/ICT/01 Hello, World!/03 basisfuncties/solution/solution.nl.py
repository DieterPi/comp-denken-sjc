#!/usr/bin/python
# -*- coding: utf-8 -*-

# vul de juiste invoer in
getal1 = int( input( 'Geef het eerste getal in: ' ) )
getal2 = int( input( 'Geef het tweede getal in: ' ) )
getal3 = int( input( 'Geef het derde getal in: ' ) )

# bereken hier het maximum, minumum en het gemiddelde
maximum = max( getal1, getal2, getal3 )
minimum = min( getal1, getal2, getal3 )
gemiddelde = round( ( getal1 + getal2 + getal3 ) / 3 , 2 )

# vul hieronder de andere uitvoer aan
print() # generator.py hack
print('maximum:', maximum )
print('minimum:', minimum )
print('gemiddelde:', gemiddelde )