#!/usr/bin/python
# -*- coding: utf-8 -*-

n = int( input( 'n = ' ) )
x = int( input( 'x = ' ) )

macht = 1
for i in  range( n ):
    macht *= x
    
print( macht ) 