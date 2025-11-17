#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def oppervlakte_koch( z ):
    A = 2 * z**2 * math.sqrt(3) / 5
    return round( A, 2 )

if __name__ == '__main__':
    import doctest
    doctest.testmod()