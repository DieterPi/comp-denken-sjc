#!/usr/bin/python
# -*- coding: utf-8 -*-

def tafel( getal ):
    for i in range( 10 ):
        print( i+1, '*', getal, '=', ( i + 1 ) * getal )

if __name__ == '__main__':
    import doctest
    doctest.testmod()