#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

# intialisatie
min = math.inf
max = -math.inf
aantal = 0

for i in range( 5 ):
    getal = int( input( 'Geef een geheel getal in: ' ) )
    if getal < min:
        min = getal
    if getal > max:
        max = getal
    aantal += int( getal % 3 == 0 )

print( 'Grootste getal:', max )
print( 'Kleinste getal:', min )
print( 'Aantal getallen deelbaar door 3:', aantal )