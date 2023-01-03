#!/usr/bin/python
# -*- coding: utf-8 -*-

def rockpaperscissors( woord1, woord2 ):
    if woord1 == woord2:
        print( 'onbeslist' )
    elif woord1 == 'paper' and woord2 == 'rock':
        print( 'speler 1 wint' )
    elif woord1 == 'rock' and woord2 == 'scissors':
        print( 'speler 1 wint' )
    elif woord1 == 'scissors' and woord2 == 'paper':
        print( 'speler 1 wint' )
    else: 
        print( 'speler 2 wint' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()