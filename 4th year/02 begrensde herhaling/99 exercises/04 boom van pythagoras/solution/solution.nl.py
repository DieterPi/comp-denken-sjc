#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def oppervlakte_boom( orde ):
    z = 1
    A = z**2
    for i in range( orde ):
        z = math.sqrt(z / 2)
        A += 2**(i+1) * z**2
    return round( A, 9 )

if __name__ == '__main__':
    import doctest
    doctest.testmod()