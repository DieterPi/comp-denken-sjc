#!/usr/bin/python
# -*- coding: utf-8 -*-

def fibonnaci( rangnummer ):
    vorige_getal = 1
    getal = 1
    if rangnummer > 2:
        for i in range( 2, rangnummer):
            nieuwe_getal = vorige_getal + getal
            vorige_getal = getal
            getal = nieuwe_getal
    return( getal )

if __name__ == '__main__':
    import doctest
    doctest.testmod()