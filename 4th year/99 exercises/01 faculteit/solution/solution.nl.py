#!/usr/bin/python
# -*- coding: utf-8 -*-

def faculteit( getal ):
    product = 1
    for i in range( 1, getal + 1 ):
        product *= i
    print( str(product) )

if __name__ == '__main__':
    import doctest
    doctest.testmod()