#!/usr/bin/python
# -*- coding: utf-8 -*-

getal = float( input( 'Geef een kommagetal in: ' ) )

print('{}'.format( int( ( getal * 10 ) % 10 ) ) )
