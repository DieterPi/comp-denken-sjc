#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

z = float( input( 'Geef de lengte van de zijde in (in cm):' ) )

A = (math.pi/6 - math.sqrt(3)/4) * z **2

print()
print( 'Oppervlakte: {} cm²'.format( round( A, 3 ) ) )