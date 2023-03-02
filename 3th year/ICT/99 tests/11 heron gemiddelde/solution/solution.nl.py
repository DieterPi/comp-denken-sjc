#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

a = int( input( 'Geef een eerste getal in: ' ) )
b = int( input( 'Geef een tweede getal in: ' ) )

h = round( 1/3 * (a + math.sqrt(a*b)+b), 1 )

print('')
print( 'Het gemiddelde van', a, 'en', b, 'is', h )