#!/usr/bin/python
# -*- coding: utf-8 -*-

def ggd( getal1, getal2 ):
    A = max(getal1, getal2)
    B = min(getal1, getal2)

    rest = A % B
    while rest != 0:
        A = B
        B = rest
        rest = A % B
    
    return B

if __name__ == '__main__':
    import doctest
    doctest.testmod()