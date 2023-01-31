#!/usr/bin/python
# -*- coding: utf-8 -*-

massa = int( input( 'Geef de gewenste massa: ') )

aantal500 = massa // 500
rest500 = massa % 500
aantal120 =  rest500 // 120
rest120 = rest500 % 120
aantal40 = rest120 // 40

print( '' )
print( 'aantal repen van 500 g:', aantal500 )
print( 'aantal repen van 120 g:', aantal120 )
print( 'aantal repen van 40 g:', aantal40 )