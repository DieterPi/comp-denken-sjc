#!/usr/bin/python
# -*- coding: utf-8 -*-

def ct_treshold( waarde ):
    if waarde <= 13.1:
        print( 'zeer sterk positief (superverspreider)' )
    elif waarde <= 19.5:
        print( 'sterk positief' )
    elif waarde <= 26.0:
        print( 'gewoon positief' )
    else:
        print( 'zwak positief' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()