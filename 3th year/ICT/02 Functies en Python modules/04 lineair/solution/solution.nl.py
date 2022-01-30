#!/usr/bin/python
# -*- coding: utf-8 -*-

def f( x ):
    y = 3 * x - 4
    return round( y, 2 )

if __name__ == '__main__':
    import doctest
    doctest.testmod()