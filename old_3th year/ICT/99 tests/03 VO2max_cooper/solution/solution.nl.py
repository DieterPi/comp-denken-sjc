#!/usr/bin/python
# -*- coding: utf-8 -*-
d12 = float( input( 'Geef het aantal meter in:' ) )

VO2max = ( d12 - 505 ) / 45

print('VO2max: {}'.format( round( VO2max, 1 ) ) )