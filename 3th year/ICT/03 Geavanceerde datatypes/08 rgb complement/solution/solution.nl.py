#!/usr/bin/python
# -*- coding: utf-8 -*-

def complementair( kleurtupel ):
    kleur = ( 255 - kleurtupel[0], 255 - kleurtupel[1], 255 - kleurtupel[2] )
    print(kleur)

if __name__ == '__main__':
    import doctest
    doctest.testmod()