#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

getal = float( input( 'Geef een getal in: ') )

lijst = [math.floor(getal), getal, math.floor(getal)+1 ]
print('\n{}'.format(lijst))