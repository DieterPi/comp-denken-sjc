#!/usr/bin/python
# -*- coding: utf-8 -*-

def volgend_collatz_getal( getal ):
    if getal % 2 == 0:
        volgend_getal = getal // 2
    else:
        volgend_getal = getal * 3 +1
    return volgend_getal

def collatz( getal ):
    lijst = [ getal ]
    while getal != 1:
        getal = volgend_collatz_getal( getal )
        lijst.append( getal )
    return lijst

if __name__ == '__main__':
    import doctest
    doctest.testmod()