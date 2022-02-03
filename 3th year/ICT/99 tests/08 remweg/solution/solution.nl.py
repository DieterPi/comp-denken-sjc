#!/usr/bin/python
# -*- coding: utf-8 -*-

snelheid = float( input( 'Geef de snelheid in km/u in:' ) )
a = float( input( 'Geef de remvertraging in m/s² in:' ) )

v = snelheid / 3.6

remweg = pow( v, 2) / ( 2 * a )

print( 'Remweg: {}'.format( round( remweg, 3 ) ) )