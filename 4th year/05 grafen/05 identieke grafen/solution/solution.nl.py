#!/usr/bin/python
# -*- coding: utf-8 -*-

def identiek( E1: list, E2: list ) -> bool:
    if len(E1) != len(E2):
        return False
    
    similar = 0
    for e1 in E1:
        for e2 in E2:
            if e1[0] in e2 and e1[1] in e2:
                similar += 1
    return similar == len( E1 )
