#!/usr/bin/python
# -*- coding: utf-8 -*-

def rekenkundig_gemiddelde( tupel ):
    som = 0
    for i in range( len( tupel ) ):
        som += tupel[i]
    return round( som / len( tupel ), 2 )

def harmonisch_gemiddelde( tupel ):
    som = 0
    for i in range( len( tupel ) ):
        som += 1 / tupel[i]
    return round( len( tupel ) / som, 2 )

if __name__ == '__main__':
    import doctest
    doctest.testmod()