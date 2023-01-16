#!/usr/bin/python
# -*- coding: utf-8 -*-

l = int( input( 'Geef de lengte in:' ) )
h = int( input( 'Geef de hoogte in:' ) )

MP = l*h / 1000000

print('\nDit komt overeen met een resolutie van {} MP.'.format( round( MP, 2 ) ) )