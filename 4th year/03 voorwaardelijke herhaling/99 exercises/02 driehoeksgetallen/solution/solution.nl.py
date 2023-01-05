#!/usr/bin/python
# -*- coding: utf-8 -*-

def driehoeksgetal( getal ):
    t = 1
    i = 1
    print( i, ':', t)
    while( t +i+1 < getal ):
        t += i+1
        i += 1
        print( i, ':', t)

if __name__ == '__main__':
    import doctest
    doctest.testmod()