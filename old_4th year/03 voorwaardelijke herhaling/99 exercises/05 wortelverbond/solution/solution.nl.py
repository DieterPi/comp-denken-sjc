#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
huidige_jaartal = datetime.date.today().year

naam = input( 'Geef de naam van de persoon in:' )
geboortejaar = int( input( 'Geef het geboortejaar in:' ) )

jaar = 0
clublid = False
while jaar < 120 and not clublid:
    jaar += 1
    clublid = jaar**2 == ( geboortejaar + jaar )

print()
if clublid:
    if geboortejaar + jaar < huidige_jaartal:
        print( naam, 'was', jaar, 'in', geboortejaar + jaar )
    else:
        print( naam, 'wordt', jaar, 'in', geboortejaar + jaar )
    
else:
    print( naam, 'is geen lid van het Verbond der Wortels' )