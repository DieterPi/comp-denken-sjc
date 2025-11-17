#!/usr/bin/python
# -*- coding: utf-8 -*-

def wissel( lijst ):
    tweede_element = lijst[ 1 ]
    lijst[ 1 ] = lijst[ len(lijst) - 2 ]
    lijst[ len(lijst) - 2 ] = tweede_element
    print(lijst)

if __name__ == '__main__':
    import doctest
    doctest.testmod()