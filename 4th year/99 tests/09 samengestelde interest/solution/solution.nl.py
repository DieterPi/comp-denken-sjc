#!/usr/bin/python
# -*- coding: utf-8 -*-

def samengesteld( startbedrag, rentevoet, aantal_jaar ):
    bedrag = startbedrag
    for i in range( aantal_jaar ):
        bedrag = round( bedrag * ( 1 + rentevoet ), 2 )
        print( 'Na jaar', i + 1 , 'is het bedrag aangegroeid tot €', bedrag )
    
    winst = bedrag - startbedrag
    jaarrente = round( winst / startbedrag / aantal_jaar *100 , 2)
    print( 'Dit komt overeen met een winst van €', winst, 'of op jaarbasis', jaarrente, '%.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()