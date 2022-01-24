#!/usr/bin/python
# -*- coding: utf-8 -*-

tekst = str( input( 'Geef een tekstfragment in: ' ) )

pos = tekst.find( ' ' )

print('{}'.format( tekst[ (pos + 1):len( tekst )] + ' ' + tekst[0:pos] ) )
