#!/usr/bin/python
# -*- coding: utf-8 -*-

massa = float( input( 'Geef de massa in: ' ) )
aantal = float( input( 'Geef het aantal in: ' ) )

if aantal >= 10:
    if massa >= 350:
        bedrag = aantal * 9.30
    elif massa >= 100:
        bedrag = aantal * 5.58
    else:
        bedrag = aantal * 3.72
else:
    if massa >= 350:
        bedrag = aantal * 9.45
    elif massa >= 100:
        bedrag = aantal * 5.67
    else:
        bedrag = aantal * 3.78

print( '\nU dient EUR', round( bedrag, 2), 'te betalen.' )