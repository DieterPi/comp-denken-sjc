#!/usr/bin/python
# -*- coding: utf-8 -*-

def verbonden_bogen( v: str, E: list ) -> list:
    connected = []
    
    for edge in E:
        if v in edge:
            connected.append( edge )
    
    return connected
