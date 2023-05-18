#!/usr/bin/python
# -*- coding: utf-8 -*-

def padovan( n ):
    p1 = 1
    p2 = 1
    p3 = 1
    p = 1
    if n <= 3:
        print( 1 )
    else: 
        for i in range( 3, n ):
            p = p2 + p1
            p1 = p2
            p2 = p3
            p3 = p
        print( p )

if __name__ == '__main__':
    import doctest
    doctest.testmod()