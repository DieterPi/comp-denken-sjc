#!/usr/bin/python
# -*- coding: utf-8 -*-
def soort_vkv( b, c ):
    if b == 0 or c == 0:
        print( 'Onvolledig' )
    else:
        print( 'Volledig' )
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()