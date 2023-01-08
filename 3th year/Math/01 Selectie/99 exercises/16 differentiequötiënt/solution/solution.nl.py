#!/usr/bin/python
# -*- coding: utf-8 -*-

def differentiequotient( koppel1, koppel2 ):
    if (koppel1[0] != koppel2[0]):
        getal = (koppel2[1] - koppel1[1]) / (koppel2[0] - koppel1[0])
        print( 'Het differentiequötiënt op het interval [', min(koppel1[0], koppel2[0]),',',max(koppel1[0], koppel2[0]),'] is:', round( getal, 2))
    else:
        print( 'Deze twee punten hebben eenzelfde x coördinaat, hier kan je dus geen differentiequötiënt berekenen' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()