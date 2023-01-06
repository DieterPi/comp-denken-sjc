#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def oppervlakte( a, b, c ):
    s = 1 / 2 * ( a + b + c )
    A = math.sqrt( s * (s - a) * ( s - b ) * ( s - c ) )
    return round( A, 2 )

if __name__ == '__main__':
    import doctest
    doctest.testmod()