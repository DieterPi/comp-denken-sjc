#!/usr/bin/python
# -*- coding: utf-8 -*-

def regula_falsi_modified( f: float, a: float , b: float, toleratie: float) -> float:
    flag = True
    y_a = f( a )
    y_b = f( b )
    while flag:
        c = a - y_a * ( b - a )/( y_b - y_a )
        if f( c ) * f( a ) < 0:
            b = c
            y_b = f( b )
            y_a /= 2
        elif f( c ) * f( b ) < 0:
            a = c
            y_a = f( a )
            y_b /= 2
        else: # f( c ) == 0
            a = c
            b = c
        flag = abs( f( c ) ) > toleratie
    return round( c, 4 )
