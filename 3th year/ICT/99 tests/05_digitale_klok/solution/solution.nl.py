#!/usr/bin/python
# -*- coding: utf-8 -*-

sec = int( input( 'Geef het aantal seconden in:' ) )

uren = sec // ( 60 * 60 )
minuten = (sec - uren * 60 * 60) // 60
seconden = sec % 60

print('\n')
print(uren,':',minuten,':',seconden)