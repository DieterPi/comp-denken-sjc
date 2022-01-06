#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

som = 0
for i in range( 2 ):
    kaart = random.randint( 1, 11 )
    print( 'Je kreeg een', kaart )
    som += kaart

if som == 22:
    print( 'Verloren' )
elif som == 21:
    print( 'Gewonnen' )
else:
    vraag = str( input( 'Verdergaan? ' ) )
    while vraag == 'J' and som < 21:
        kaart = random.randint( 1, 11 )
        print( 'Je kreeg een', kaart )
        som += kaart
        if som < 21:
            vraag = str( input( 'Verdergaan? ' ) )

if som > 21:
    print( 'Verloren' )
elif som == 21:
    print( 'Gewonnen' )
else:
    print( 'Voorzicht gespeeld' )
