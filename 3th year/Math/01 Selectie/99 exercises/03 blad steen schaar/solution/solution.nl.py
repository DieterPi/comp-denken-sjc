#!/usr/bin/python
# -*- coding: utf-8 -*-

def bladsteenschaar( woord1, woord2 ):
    if woord1 == woord2:
        print( 'onbeslist' )
    elif woord1 == 'blad' and woord2 == 'steen':
        print( 'speler 1 wint' )
    elif woord1 == 'steen' and woord2 == 'schaar':
        print( 'speler 1 wint' )
    elif woord1 == 'schaar' and woord2 == 'blad':
        print( 'speler 1 wint' )
    else: 
        print( 'speler 2 wint' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()