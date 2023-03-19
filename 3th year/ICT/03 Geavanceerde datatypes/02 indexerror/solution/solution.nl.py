#!/usr/bin/python
# -*- coding: utf-8 -*-

def laatste_element( tupel ):
    lengte = len( tupel )
    print( tupel[lengte - 1] )

if __name__ == '__main__':
    import doctest
    doctest.testmod()