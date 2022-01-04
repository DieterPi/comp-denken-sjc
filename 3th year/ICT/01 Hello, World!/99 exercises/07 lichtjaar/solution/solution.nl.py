#!/usr/bin/python
# -*- coding: utf-8 -*-

c = 299792458
lj = c*365.25*24*60*60

afstand = float( input( 'Geef een aantal km in ' ) )

print('\nAfstand in lichtjaar: {}'.format(round( afstand * 1000 / lj, 9 ) ) )
