#!/usr/bin/python
# -*- coding: utf-8 -*-

V_ref = float( input( 'Geef de V_ref in: ' ) )

I = round( V_ref / ( 8 * 0.05 ), 3 )

print('De stroomsterkte is {}'.format( I ) )