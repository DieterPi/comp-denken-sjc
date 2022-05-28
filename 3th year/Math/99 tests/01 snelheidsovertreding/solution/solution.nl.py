#!/usr/bin/python
# -*- coding: utf-8 -*-

def boete( snelheid ):
    overschot = snelheid - 50
    if( overschot < 0 ):
        print( 'Niet in overtreding' )
    elif( overschot < 11 ):
        print( 'Boete: EUR 53' )
    elif( overschot <= 30 ):
        bedrag = 53 + 11 * overschot
        print( 'Boete: EUR', bedrag )
    else:
        print( 'Invoering rijbewijs en rechtzaak' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()