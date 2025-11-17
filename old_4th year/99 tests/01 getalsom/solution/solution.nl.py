#!/usr/bin/python
# -*- coding: utf-8 -*-

def getalsom( getal ):
    som = 0
    while getal > 0:
        som += getal % 10
        getal //= 10
    print( som )

if __name__ == '__main__':
    import doctest
    doctest.testmod()