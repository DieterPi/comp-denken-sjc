#!/usr/bin/python
# -*- coding: utf-8 -*-

T_C = float( input( 'Geef een temperatuur in °C: ' ) )

T_F = round( 9 / 5 * T_C + 32, 2 )

print( '\ntemperatuur: {} °F'.format(T_F) )