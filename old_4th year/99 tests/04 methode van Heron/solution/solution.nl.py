#!/usr/bin/python
# -*- coding: utf-8 -*-

def babylonische_methode( grondtal, startwaarde ):
    getal1 = startwaarde
    verschil = 1
    i = 0
    while verschil > pow( 10, -12):
        getal2 = 1/2 * (getal1 + grondtal / getal1)
        print(i,':',  getal1 )
        verschil = abs(getal2 - getal1)
        getal1 = getal2
        i += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()