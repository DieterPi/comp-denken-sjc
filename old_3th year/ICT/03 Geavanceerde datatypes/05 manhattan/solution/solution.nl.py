#!/usr/bin/python
# -*- coding: utf-8 -*-
def manhattan( punt1, punt2):
    d = round( abs( punt1[0] - punt2[0] ) + abs( punt1[1] - punt2[1] ), 1)
    print(d)

if __name__ == '__main__':
    import doctest
    doctest.testmod()