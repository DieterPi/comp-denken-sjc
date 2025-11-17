#!/usr/bin/python
# -*- coding: utf-8 -*-
def euler_formule( h, r, z ):
    return h - r + z == 2

if __name__ == '__main__':
    import doctest
    doctest.testmod()