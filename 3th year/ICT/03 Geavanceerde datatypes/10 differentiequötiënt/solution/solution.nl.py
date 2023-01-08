#!/usr/bin/python
# -*- coding: utf-8 -*-

def differentiequotient( koppel1, koppel2 ):
    getal = (koppel2[1] - koppel1[1]) / (koppel2[0] - koppel1[0])
    print( 'Het differentiequötiënt op dit interval is:', round( getal, 2))

if __name__ == '__main__':
    import doctest
    doctest.testmod()