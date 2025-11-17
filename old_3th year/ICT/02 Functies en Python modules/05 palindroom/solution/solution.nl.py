#!/usr/bin/python
# -*- coding: utf-8 -*-

def palindroom( getal ):
    H = getal // 100
    T = ( getal % 100 ) // 10 
    E = getal % 10
    
    palindroomgetal = getal * pow( 10, 3) + E * 100 + T * 10 + H
    return palindroomgetal

if __name__ == '__main__':
    import doctest
    doctest.testmod()