#!/usr/bin/python
# -*- coding: utf-8 -*-
def discriminant( a, b, c ):
    D = b**2 - 4 * a * c
    print( 'Discriminant =', D )
    if D > 0:
        print( 'Er zijn twee verschillende oplossingen')
    elif D < 0:
        print( 'Er zijn geen oplossingen')
    else:
        print( 'Er is exact één oplossing')
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()