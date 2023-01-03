#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_perfect( getal ):
    som = 0
    for i in range( 1, getal ):
        if getal % i == 0:
            som += i
    return som == getal

if __name__ == '__main__':
    import doctest
    doctest.testmod()