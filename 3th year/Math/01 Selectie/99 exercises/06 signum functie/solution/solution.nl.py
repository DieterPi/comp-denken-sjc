#!/usr/bin/python
# -*- coding: utf-8 -*-

def sgn( x ):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()