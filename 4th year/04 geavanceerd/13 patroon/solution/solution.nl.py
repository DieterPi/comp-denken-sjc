#!/usr/bin/python
# -*- coding: utf-8 -*-

def schaakbord( rows: int , cols: int ) -> None:
    teller = 0
    for r in range( rows ):
        for k in range( cols ):
            if ( r + k ) % 2 == 0:
                print('x', end = ' ' )
            else:
                print('.', end = ' ' )
        print( )
