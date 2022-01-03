#!/usr/bin/python
# -*- coding: utf-8 -*-

lengte = float( input( 'Geef een lengte in m in: ' ) )

inch = 2.54 / 100
foot = 12 * inch
yard = 3 * foot

aantal_yard = lengte // yard
rest = lengte - aantal_yard * yard
aantal_foot = rest // foot
rest = rest - aantal_foot * foot
aantal_inch = round(rest / inch, 2)

print('\nDit stemt overeen met {} yard {} feet {} inch'.format( aantal_yard, aantal_foot, aantal_inch ) )