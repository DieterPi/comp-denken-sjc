#!/usr/bin/python
# -*- coding: utf-8 -*-

PI = 3.141592

r = float( input( 'Geef de straal in:' ) )
h = float( input( 'Geef de hoogte in:' ) )

A = 2 * PI * r * h + 2 * PI * r**2
V = PI * r**2 * h

print('\nOppervlakte: {} cm²'.format( round( A, 3 ) ) )
print('Volume: {} cm³'.format( round( V, 3 ) ) )