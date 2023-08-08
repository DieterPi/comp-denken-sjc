#!/usr/bin/python
# -*- coding: utf-8 -*-

def benedendriehoeksmatrix( n: int ) -> None:
    for r in range( n ):
        for k in range( n ): 
            print( max( r - k + 1, 0 ) , end = ' ' )
        print()
