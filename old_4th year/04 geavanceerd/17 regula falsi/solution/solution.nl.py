#!/usr/bin/python
# -*- coding: utf-8 -*-

def regula_falsi( f: float, a: float , b: float, toleratie: float) -> float:
    flag = True
    while flag:
        c = a - f( a ) * ( b - a )/( f( b ) - f( a ) )
        if f( c ) * f( a ) < 0:
            b = c
        elif f( c ) * f( b ) < 0:
            a = c
        else: # f( c ) == 0
            a = c
            b = c
        flag = abs( f( c ) ) > toleratie
    return round( c, 4 )
