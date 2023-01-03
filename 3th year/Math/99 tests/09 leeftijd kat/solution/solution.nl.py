#!/usr/bin/python
# -*- coding: utf-8 -*-

katjaar = int( input( 'Geef het aantal katjaren in: ' ) )

if katjaar == 1:
    mensjaar = 15
elif katjaar == 2:
    mensjaar = 15 + 9
else:
    mensjaar = 15 + 9 + ( katjaar - 2 ) * 4

print('')
print( 'Een kat van', katjaar, 'is', mensjaar, 'jaar in mensenjaren!' )
