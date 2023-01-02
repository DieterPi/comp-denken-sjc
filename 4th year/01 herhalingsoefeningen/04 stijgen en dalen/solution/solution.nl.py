#!/usr/bin/python
# -*- coding: utf-8 -*-
def soort_rechte( rico ):
    if rico > 0:
        print( 'De rechte is stijgend.' )
    elif rico < 0:
        print( 'De rechte is dalend.' )
    else:
        print( 'De rechte is constant.' )
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()