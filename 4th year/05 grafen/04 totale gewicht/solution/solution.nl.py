#!/usr/bin/python
# -*- coding: utf-8 -*-

def gewicht( E: list ) -> int:
    weight = 0
    for edge in E:
        weight += edge[2]
    
    return weight
