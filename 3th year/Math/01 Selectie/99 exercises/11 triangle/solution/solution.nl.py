#!/usr/bin/python
# -*- coding: utf-8 -*-

def soort_driehoek( a, b, c ):
    if( a == b or a == c or b == c):
        if (a == b and b == c):
            print ( 'Gelijkzijdig' )
        else:
            print( 'Gelijkbenig' )
    else:
        print( 'Willekeurig' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()