#!/usr/bin/python
# -*- coding: utf-8 -*-

def diagonaal( n ):
    for r in range( n ):
        for k in range( n ): 
            print( abs( k - r ) , end = ' ')
        print( )
