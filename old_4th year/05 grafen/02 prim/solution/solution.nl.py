#!/usr/bin/python
# -*- coding: utf-8 -*-
def is_connected( vertex: str, edge: tuple ) -> bool:
    return vertex in edge

def other_vertex( edge: list, vertex: str ) -> list:
    if edge[0] == vertex:
        other_vertex = edge[1]
    else:
        other_vertex = edge[0]
    return other_vertex

def MST_prim( V: list, E: list ) -> list:
    tree = []
    
    v1 = V[0] # starting vertex, can be chosen at random

    V.remove(v1) # remaining vertices
    connected_v = [ v1 ]
    while len( V ) > 0:
        min_val = 10**100
        for v in connected_v:
            for e in E:
                if is_connected( v, e ) and other_vertex( e, v ) in V :
                    # this is a vertex connected to the initial vertex
                    # and the other endpoint hasn't been connected yet
                    # now checking if it's minimal
                    if e[2] < min_val: 
                        min_val = e[2]
                        min_edge = e
                        if e[0] in connected_v:
                            min_vertex = e[1]
                        else:
                            min_vertex = e[0]
        
        # has looped through every vertex in MST and every available edge
        connected_v.append( min_vertex )

        tree.append( min_edge )
        E.remove( min_edge )
        V.remove( min_vertex )
    
    return tree
