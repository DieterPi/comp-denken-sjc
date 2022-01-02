#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def meetkundig_gemiddelde( a, b ):
    mean = round( math.sqrt(a*b), 2)
    return mean

if __name__ == '__main__':
    import doctest
    doctest.testmod()