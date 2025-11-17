#!/usr/bin/python
# -*- coding: utf-8 -*-

def sgn( x ):
    if x < 0:
        output = -1
    elif x > 0:
        output = 1
    else:
        output = 0
    print(output)

if __name__ == '__main__':
    import doctest
    doctest.testmod()