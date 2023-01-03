#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

getal = random.randint( 1, 1000 )

gok = int( input( 'Gok een getal: ' ) )
aantal = 1
while gok != getal:
    if gok < getal:
        print( 'Hoger' )
    else:
        print( 'Lager' )
    gok = int( input( 'Gok een getal: ' ) )
    aantal += 1

print( 'Aantal pogingen: ', aantal )