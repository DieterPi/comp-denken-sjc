#!/usr/bin/python
# -*- coding: utf-8 -*-

def driehoek( a, b, c ):
    if( a + b > c and b + c > a and a + c > b):
        print( 'Deze zijden vormen een driehoek.' )
    else:
        print( 'Deze zijden vormen geen driehoek.' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()