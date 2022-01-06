#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def bazel_benadering( aantal ):
    som = 0
    for i in range( aantal ):
        som += 1/pow( i + 1, 2 )
    return round( math.sqrt( 6 * som ), 9 )

if __name__ == '__main__':
    import doctest
    doctest.testmod()