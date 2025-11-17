#!/usr/bin/python
# -*- coding: utf-8 -*-

def ibu( waarde ):
    if waarde < 20:
        print( 'Dit bier is weinig bitter.' )
    elif waarde < 30:
        print( 'Dit bier neigt naar bitter.' )
    elif waarde < 40:
        print( 'Dit bier is bitter.' )
    else:
        print( 'Dit bier is zeer bitter.' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()