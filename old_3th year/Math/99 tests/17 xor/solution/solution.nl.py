#!/usr/bin/python
# -*- coding: utf-8 -*-

def xor( A, B ):
    X = (A or B)  and not (A and B)
    print( X )

if __name__ == '__main__':
    import doctest
    doctest.testmod()