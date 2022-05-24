#!/usr/bin/python
# -*- coding: utf-8 -*-

def aantal_dagen( maandnummer ):
    if (maandnummer % 2 == 0):
        if( maandnummer == 2):
            print( 'Maand', maandnummer, 'bevat 28 dagen.')
        else:
            print( 'Maand', maandnummer, 'bevat 30 dagen.')
    else:
        print( 'Maand', maandnummer, 'bevat 31 dagen.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()