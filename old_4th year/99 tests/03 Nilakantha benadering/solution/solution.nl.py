#!/usr/bin/python
# -*- coding: utf-8 -*-

def nilakantha_benadering( aantal ):
    som = 0
    for i in range( aantal ):
        som += (-1)**(i) / ((3 + i*2 -1) * (3 + i*2) * (3 + i*2+1) )
    print( round( 3+4 * som, 9 ) )

if __name__ == '__main__':
    import doctest
    doctest.testmod()