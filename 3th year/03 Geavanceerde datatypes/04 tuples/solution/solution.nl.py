#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def afstand( coordinaat ):
    d = round( math.sqrt( pow( coordinaat[0], 2) + pow( coordinaat[1], 2) ), 2)
    return d

if __name__ == '__main__':
    import doctest
    doctest.testmod()