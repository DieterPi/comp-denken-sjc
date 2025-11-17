#!/usr/bin/python
# -*- coding: utf-8 -*-

def kostprijs( aantal ):
    bedrag = aantal * 3.29
    if( aantal == 2 ):
        print( round( bedrag * 0.8, 2 ) )
    elif( aantal > 2 ):
        print( round( bedrag * 0.7, 2 ) )
    else:
        print( round( bedrag, 2 ) ) 

if __name__ == '__main__':
    import doctest
    doctest.testmod()