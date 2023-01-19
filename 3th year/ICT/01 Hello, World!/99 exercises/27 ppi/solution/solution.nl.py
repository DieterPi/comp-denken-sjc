#!/usr/bin/python
# -*- coding: utf-8 -*-

b = int( input( 'Geef de breedte in:' ) )
h = int( input( 'Geef de hoogte in:' ) )
ppi = int( input( 'Geef de dichtheid in'))

nb = round( b / ppi * 2.54, 3)
nh = round( h / ppi * 2.54, 3)

print('')
print('Deze foto kan je afdrukken op', nb, 'x', nh, 'cm.')