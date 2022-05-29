#!/usr/bin/python
# -*- coding: utf-8 -*-

def soort_driehoek( a, b, c ):
    if a >= b and a >= c:
        val1 = a*a
        val2 = b*b+c*c
    elif b >= c:
        val1 = b*b
        val2 = a*a+c*c
    else:
        val1 = c*c
        val2 = b*b+a*a
    
    if val1 > val2:
        print( 'De driehoek is stomphoekig.' )
    elif val1 < val2:
        print( 'De driehoek is scherphoekig.' )
    else:
        print( 'De driehoek is rechthoekig.' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()