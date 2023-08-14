#!/usr/bin/python
# -*- coding: utf-8 -*-

def verbonden_knopen( v: str, E: list ) -> list:
    connected = []
    
    for edge in E:
        for i in range( 2 ):
            if edge[i] == v and edge[( i + 1 ) % 2] not in connected:
                connected.append( edge[( i + 1 ) % 2] )
    
    connected.sort()
    return connected
