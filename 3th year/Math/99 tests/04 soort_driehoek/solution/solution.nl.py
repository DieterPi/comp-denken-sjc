#!/usr/bin/python
# -*- coding: utf-8 -*-

def soort_driehoek( a, b, c ):
    if a >= b and a >= c:
        if a*a > b*b + c*c:
            print( 'De driehoek is stomphoekig.' )
        elif a*a < b*b + c*c:
            print( 'De driehoek is scherphoekig.' )
        else:
            print( 'De driehoek is rechthoekig.' )
    elif b >= c:
        if b*b > a*a + c*c:
            print( 'De driehoek is stomphoekig.' )
        elif b*b < a*a + c*c:
            print( 'De driehoek is scherphoekig.' )
        else:
            print( 'De driehoek is rechthoekig.' )
    else:
        if c*c > b*b + a*a:
            print( 'De driehoek is stomphoekig.' )
        elif c*c < b*b + a*a:
            print( 'De driehoek is scherphoekig.' )
        else:
            print( 'De driehoek is rechthoekig.' )
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()