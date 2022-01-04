#!/usr/bin/python
# -*- coding: utf-8 -*-

def laaste_element( lijst ):
    lengte = len( lijst )
    return( lijst[lengte - 1] )

if __name__ == '__main__':
    import doctest
    doctest.testmod()