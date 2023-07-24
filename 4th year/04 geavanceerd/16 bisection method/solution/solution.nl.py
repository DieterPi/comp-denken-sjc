#!/usr/bin/python
# -*- coding: utf-8 -*-

def bisectiemethode( f: float, a: float , b: float, toleratie: float) -> float:
    while b - a > toleratie:
        c = ( b + a ) / 2
        if f( c ) * f( a ) < 0:
            b = c
        elif f( c ) * f( b ) < 0:
            a = c
        else: # f( c ) == 0
            a = c
            b = c
        print( round( c, 4 ))
    return round( c, 4 )
