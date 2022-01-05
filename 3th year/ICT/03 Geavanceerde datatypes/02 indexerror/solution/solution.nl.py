#!/usr/bin/python
# -*- coding: utf-8 -*-

def laatste_element( lijst ):
    lengte = len( lijst )
    print( lijst[lengte - 1] )

if __name__ == '__main__':
    import doctest
    doctest.testmod()