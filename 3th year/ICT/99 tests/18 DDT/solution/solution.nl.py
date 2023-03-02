#!/usr/bin/python
# -*- coding: utf-8 -*-

b = int( input( 'Geef het aantal gram in: ' ) )
n = int( input( 'Geef het aantal jaar in: ' ) )

r = round( b * pow( 2, -n/15 ), 1)


print()
print('Na', n, 'jaar is er', r, 'g DDT over.')