#!/usr/bin/python
# -*- coding: utf-8 -*-

def diagonaal( n ):
    for r in range( n ):
        tekst = ''
        for k in range( n ): 
            tekst += ' ' + str( abs( k - r) ) + ' '
        print( tekst )

if __name__ == '__main__':
    import doctest
    doctest.testmod()
