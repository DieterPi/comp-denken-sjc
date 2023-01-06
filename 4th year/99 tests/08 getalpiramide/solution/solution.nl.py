#!/usr/bin/python
# -*- coding: utf-8 -*-

def getalpiramide( getal ):
    piramide = 0
    for i in range( getal ):
        piramide = piramide * 10 + ( i + 1)
        print( piramide )

if __name__ == '__main__':
    import doctest
    doctest.testmod()