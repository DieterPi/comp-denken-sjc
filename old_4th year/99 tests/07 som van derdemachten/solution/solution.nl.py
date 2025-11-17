#!/usr/bin/python
# -*- coding: utf-8 -*-

def derdemachtsom( getal ):
    som = 0
    for i in range( getal ):
        som += ( i + 1 )**3
    return som

if __name__ == '__main__':
    import doctest
    doctest.testmod()