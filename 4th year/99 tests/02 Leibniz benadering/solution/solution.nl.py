#!/usr/bin/python
# -*- coding: utf-8 -*-

def leibniz_benadering( aantal ):
    som = 0
    for i in range( aantal ):
        som += (-1)**(i) / ( 2*i +1)
    print( round( 4 * som, 9 ) )

if __name__ == '__main__':
    import doctest
    doctest.testmod()