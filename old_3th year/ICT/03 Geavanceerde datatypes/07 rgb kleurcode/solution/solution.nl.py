#!/usr/bin/python
# -*- coding: utf-8 -*-

def RGB( kleurtupel ):
    print('Rood:', kleurtupel[0])
    print('Groen:', kleurtupel[1])
    print('Blauw:', kleurtupel[2])

if __name__ == '__main__':
    import doctest
    doctest.testmod()