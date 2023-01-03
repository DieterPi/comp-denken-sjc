#!/usr/bin/python
# -*- coding: utf-8 -*-

n = int( input( 'Geef n = ' ) )
x = int( input( 'Geef x = ' ) )

macht = 1
for i in  range( n ):
    macht *= x
    
print()
print( macht ) 