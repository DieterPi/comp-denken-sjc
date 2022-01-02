#!/usr/bin/python
# -*- coding: utf-8 -*-

def harmonisch_gemiddelde( a, b ):
    harm_mean = round( 2 / ( 1 / a + 1 / b ), 2)
    return harm_mean

if __name__ == '__main__':
    import doctest
    doctest.testmod()