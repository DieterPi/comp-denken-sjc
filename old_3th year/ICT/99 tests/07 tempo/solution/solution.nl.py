#!/usr/bin/python
# -*- coding: utf-8 -*-

snelheid = float( input( 'Geef een snelheid in km/u in:' ) )

tempo = 60 / snelheid

print( '{}'.format( round( tempo, 2 ) ) )