#!/usr/bin/python
# -*- coding: utf-8 -*-

def koordenmethode( f: float, x1: float , x2: float, toleratie: float ) -> float:
    flag = True
    i = 1
    while flag:
        c = x1 - f(x1) * ( x2 - x1 )/( f(x2) - f(x1) )
        x1 = x2
        x2 = c
        flag = abs( f( c ) ) > toleratie and i < 50
    return round( c, 4 )
