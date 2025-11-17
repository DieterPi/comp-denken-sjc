#!/usr/bin/python
# -*- coding: utf-8 -*-

start = float( input( 'Geef je startkm in: ' ) )
doel = float( input( 'Geef je doelkm in: ' ) )

i = 1
print()
print( 'In week', i, 'loop je afstanden tot', round( start, 1 ), 'km.')
while start < doel:
    start *= 1.1
    i += 1
    print( 'In week', i, 'loop je afstanden tot', round( start, 1 ) , 'km.')