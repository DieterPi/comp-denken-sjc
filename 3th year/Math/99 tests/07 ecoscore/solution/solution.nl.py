#!/usr/bin/python
# -*- coding: utf-8 -*-

def ecoscore( score ):
    if( score <= 20):
        print( 'E' )
    elif( score <= 40):
        print( 'D' )
    elif( score <= 60):
        print( 'C' )
    elif( score <= 40):
        print( 'B' )
    else:
        print( 'A' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()