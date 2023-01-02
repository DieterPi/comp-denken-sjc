#!/usr/bin/python
# -*- coding: utf-8 -*-

def complementair( kleurtupel ):
    kleur = ( ( 255 - kleurtupel[0] ) % 256, ( 255 - kleurtupel[1]) % 256, ( 255 - kleurtupel[2] ) % 256 )
    print(kleur)

if __name__ == '__main__':
    import doctest
    doctest.testmod()