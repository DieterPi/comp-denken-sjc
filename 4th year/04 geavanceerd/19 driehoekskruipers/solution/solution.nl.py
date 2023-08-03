#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

n_sim = 100000
totaal_dagen = 0
for i in range( n_sim ):
    dag = 1
    
    a = random.randint(1, 3)
    if a != 3:
        dag += 1
        b = random.randint(1, 2)
        while b != 2:
            dag += 1
            b = random.randint(1, 2)
    
    totaal_dagen += dag
    
print( round( totaal_dagen / n_sim, 4) )
