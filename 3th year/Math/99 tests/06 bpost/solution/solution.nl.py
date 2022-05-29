#!/usr/bin/python
# -*- coding: utf-8 -*-

massa = float( input( 'Geef de massa in: ' ) )
aantal = float( input( 'Geef het aantal in: ' ) )

if aantal >= 10:
    if massa >= 350:
        multi = 9.30
    elif massa >= 100:
        multi = 5.58
    else:
        multi = 3.72
else:
    if massa >= 350:
        multi = 9.45
    elif massa >= 100:
        multi = 5.67
    else:
        multi = 3.78

print( '\nU dient EUR', round( aantal * multi, 2), 'te betalen.' )