#!/usr/bin/python
# -*- coding: utf-8 -*-

def schrikkeljaar( jaartal ):
    if (jaartal % 4 == 0 and jaartal % 100 != 0) or jaartal % 400 == 0:
        print( 'Een schrikkeljaar' )
    else:
        print( 'Geen schrikkeljaar' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()