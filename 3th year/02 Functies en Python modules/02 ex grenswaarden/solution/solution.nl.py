#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

getal = float( input( 'Geef een getal in: ') )

lijst = [ math.floor(getal), getal, math.ceil(getal) ]
print('\n{}'.format(lijst))