#!/usr/bin/python
# -*- coding: utf-8 -*-

def tafel( getal ):
    i = 1
    while i <= 10:
        print( i, '*', getal, '=', i * getal )
        i += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()