#!/usr/bin/python
# -*- coding: utf-8 -*-

def rekenkundig_gemiddelde( tupel ):
    som = 0
    for getal in tupel:
        som += getal
    return round( som / len( tupel ), 2 )

def harmonisch_gemiddelde( tupel ):
    som = 0
    for getal in tupel:
        som += 1 / getal
    return round( len( tupel ) / som, 2 )

if __name__ == '__main__':
    import doctest
    doctest.testmod()