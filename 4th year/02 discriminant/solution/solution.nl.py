#!/usr/bin/python
# -*- coding: utf-8 -*-
def discriminant( a, b, c ):
    D = b**2 - 4 * a * c
    print( 'Discriminant =', D )
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()