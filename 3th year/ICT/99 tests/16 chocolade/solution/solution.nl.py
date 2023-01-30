#!/usr/bin/python
# -*- coding: utf-8 -*-

massa = int( input( 'Geef de gewenste massa: ') )

aantal400 = massa // 400
rest400 = massa % 400
aantal130 =  rest400 // 130
rest130 = rest400 % 130
aantal40 = rest130 // 40

print( '' )
print( 'aantal repen van 400 g:', aantal400 )
print( 'aantal repen van 130 g:', aantal130 )
print( 'aantal repen van 40 g:', aantal40 )