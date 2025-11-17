#!/usr/bin/python
# -*- coding: utf-8 -*-

def rechthoekig( a, b, c ):
    if( a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b):
        print( 'De driehoek is rechthoekig.' )
    else:
        print( 'De driehoek is niet rechthoekig.' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()