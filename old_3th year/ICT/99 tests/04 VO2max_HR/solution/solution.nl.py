#!/usr/bin/python
# -*- coding: utf-8 -*-

HR_max = float( input( 'Geef de maximale hartslag in:' ) )
HR_rest = float( input( 'Geef de hartslag in rust in:' ) )

VO2max = 15 * HR_max / HR_rest

print('\nVO2max: {}'.format( round( VO2max, 1 ) ) )