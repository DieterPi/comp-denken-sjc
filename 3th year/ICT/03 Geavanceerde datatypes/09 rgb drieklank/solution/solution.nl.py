#!/usr/bin/python
# -*- coding: utf-8 -*-

def drieklank( kleurtupel ):
    kleur1 = ( kleurtupel[2], kleurtupel[0], kleurtupel[1] )
    kleur2 = ( kleurtupel[1], kleurtupel[2], kleurtupel[0] )
    print(kleur1)
    print(kleur2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()