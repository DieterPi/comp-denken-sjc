#!/usr/bin/python
# -*- coding: utf-8 -*-

def vijfhoeksgetal( getal ):
    t = 1
    i = 1
    print( i, ':', t)
    while t + i + 1 + 2 * i < getal :
        i += 1
        t += i + 2*( i - 1 )
        print( i, ':', t)

if __name__ == '__main__':
    import doctest
    doctest.testmod()