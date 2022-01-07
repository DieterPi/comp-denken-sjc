#!/usr/bin/python
# -*- coding: utf-8 -*-

def kleur( coordinaat ):
    if ( coordinaat[0] + coordinaat[1] ) % 2 == 0:
        print( 'Een donker gekleurd veld' )
    else:
        print( 'Een licht gekleurd veld' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()