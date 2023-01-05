#!/usr/bin/python
# -*- coding: utf-8 -*-

a = float( input( 'Geef de startwaarde in:' ) )
q = float( input( 'Geef het quotiënt in:' ) )

print()
term = a
som = a
i = 1
while som < 500:
    print( i, ':', round( som, 2) )
    term *= q
    som += term
    i += 1