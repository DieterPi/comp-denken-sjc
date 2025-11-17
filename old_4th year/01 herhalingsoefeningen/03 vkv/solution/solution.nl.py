#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def vkv( a, b, c ):
    D = b**2 - 4*a*c
    if D < 0 :
        print( 'Er zijn geen reële oplossingen' )
    elif D == 0:
        x = -b / ( 2 * a )
        print( 'Er is één oplossing, namelijk:', round( x, 2 ) )
    else:
        x1 = ( -b + math.sqrt( D ) ) / ( 2 * a )
        x2 = ( -b - math.sqrt( D ) ) / ( 2 * a )
        print( 'Er zijn 2 reële oplossingen, namelijk', round( x1, 2 ), 'en', round( x2, 2 ) )
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()