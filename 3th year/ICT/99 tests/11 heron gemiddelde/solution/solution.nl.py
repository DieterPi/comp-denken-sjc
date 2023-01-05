#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def heron_gemiddelde( a, b ):
    h = 1/3 * (a + math.sqrt(a*b)+b)
    print( round( h , 2 ) )

if __name__ == '__main__':
    import doctest
    doctest.testmod()